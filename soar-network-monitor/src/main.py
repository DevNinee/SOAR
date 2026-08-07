from network.network_info import selecionar_interface

#definir uma rede

def solicitar_confirmação(rede):
  """
  Mostrar a rede selecionada e perguntar se o usuario deseja continuar """
print("=" * 50)
print("SOAR DE DISPOSITIVOS DE REDE LOCAL")
print("=" * 50)
print(f"Rede selecionada: {rede}")

resposta = input("deseja iniciar o escaneamento? [y/n]")
if resposta == "y"
  print("Scanner autorizado! iniciando...")
     return True
  print("escaneamento cancelado!")
     return False 

def main()
'''função principal do programa'''

rede_alvo = 192.168.1.0/24
autorizada = solicitar_confirmação(rede)
 if autorizada:
   print(f"iniciando a analise da rede!{rede}...")
 else:
   print("O programa sera encerrado!")

if name == "__main__":
  main()

def solicitar_confirmacao(rede: str) -> bool:
    print(f"\nRede selecionada: {rede}")

    resposta = input(
        "Deseja iniciar o escaneamento? [s/N]: "
    ).strip().lower()

    return resposta in {"s", "sim"}


def main() -> None:
    print("=" * 55)
    print("SOAR DE DISPOSITIVOS DE REDE LOCAL")
    print("=" * 55)

    interface = selecionar_interface()

    if interface is None:
        print("Não foi possível selecionar uma interface.")
        return

    print("\nInterface escolhida:")
    print(f"Nome:     {interface.nome}")
    print(f"IPv4:     {interface.ipv4}")
    print(f"Máscara:  {interface.mascara}")
    print(f"Rede:     {interface.rede}")

    autorizado = solicitar_confirmacao(interface.rede)

    if not autorizado:
        print("Operação cancelada.")
        return

    print(
        f"O escaneamento da rede {interface.rede} "
        f"será iniciado pela interface {interface.nome}."
    )

    # O scanner ARP será chamado aqui futuramente.


if __name__ == "__main__":
    main()


