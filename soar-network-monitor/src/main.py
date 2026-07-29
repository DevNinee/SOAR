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

