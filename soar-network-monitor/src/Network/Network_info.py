
import ipaddress
import socket
from dataclasses import dataclass

import psutil


@dataclass
class InterfaceRede:
    nome: str
    ipv4: str
    mascara: str
    rede: str
    ativa: bool


def endereco_loopback(ip: str) -> bool:
    """
    Verifica se o endereço pertence à própria máquina,
    como 127.0.0.1.
    """
    return ipaddress.ip_address(ip).is_loopback


def endereco_apipa(ip: str) -> bool:
    """
    Verifica se o endereço está na faixa automática
    169.254.0.0/16.
    """
    return ipaddress.ip_address(ip).is_link_local


def calcular_rede(ip: str, mascara: str) -> str:
    """
    Calcula a faixa de rede usando o endereço IPv4
    e sua máscara.
    """
    interface = ipaddress.ip_interface(f"{ip}/{mascara}")
    return str(interface.network)


def listar_interfaces_ipv4() -> list[InterfaceRede]:
    """
    Lista as interfaces IPv4 válidas da máquina.
    Funciona em Windows, Linux e macOS.
    """
    enderecos = psutil.net_if_addrs()
    estados = psutil.net_if_stats()

    interfaces: list[InterfaceRede] = []

    for nome, lista_enderecos in enderecos.items():
        estado = estados.get(nome)
        esta_ativa = estado.isup if estado else False

        for endereco in lista_enderecos:
            if endereco.family != socket.AF_INET:
                continue

            ip = endereco.address
            mascara = endereco.netmask

            if not mascara:
                continue

            if endereco_loopback(ip):
                continue

            if endereco_apipa(ip):
                continue

            rede = calcular_rede(ip, mascara)

            interface = InterfaceRede(
                nome=nome,
                ipv4=ip,
                mascara=mascara,
                rede=rede,
                ativa=esta_ativa,
            )

            interfaces.append(interface)

    return interfaces


def obter_interfaces_ativas() -> list[InterfaceRede]:
    """
    Retorna apenas interfaces que estão marcadas
    como ativas pelo sistema operacional.
    """
    interfaces = listar_interfaces_ipv4()

    return [
        interface
        for interface in interfaces
        if interface.ativa
    ]


def selecionar_interface() -> InterfaceRede | None:
    """
    Permite que o usuário escolha qual interface
    será usada pelo scanner.
    """
    interfaces = obter_interfaces_ativas()

    if not interfaces:
        print("Nenhuma interface IPv4 ativa foi encontrada.")
        return None

    print("\nInterfaces IPv4 disponíveis:\n")

    for indice, interface in enumerate(interfaces, start=1):
        print(
            f"[{indice}] {interface.nome}\n"
            f"    IPv4:    {interface.ipv4}\n"
            f"    Máscara: {interface.mascara}\n"
            f"    Rede:    {interface.rede}\n"
        )

    resposta = input("Escolha a interface: ").strip()

    try:
        indice_escolhido = int(resposta) - 1
        return interfaces[indice_escolhido]

    except ValueError:
        print("Digite apenas o número da interface.")
        return None

    except IndexError:
        print("A opção escolhida não existe.")
        return None