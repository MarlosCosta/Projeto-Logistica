#Atividade 03 de 04 do Trabalho
#Inicio da função dimensoesObjeto()
def dimensoesObjeto():
    print("-----Dimensões do Objeto-----")
    volumeObjeto = 0
    while True:
        altura = input("Digite o altura do objeto (em cm): ")
        comprimento = input("Digite o comprimento do objeto (em cm): ")
        largura = input("Digite a largura do objeto (em cm): ")
        if not altura.isdigit() and comprimento.isdigit() and largura.isdigit():
            print("Você digitou alguma dimensão do objeto com valor não númerico!")
            continue
        else:
            altura = float(altura)
            comprimento = float(comprimento)
            largura = float(largura)
        volumeObjeto = altura * comprimento * largura
        print("O volume do objeto é (em cm³) : {:.2f}" .format(volumeObjeto))
        if volumeObjeto >= 100000:
            print("Não aceitamos objeto com dimensões tão grandes")
            continue
        break
#Fim da função dimensoesObjeto()

#Inicio da função pesoObjeto()
def pesoObjeto():
    print("-----Peso do Objeto-----")
    while True:
        peso = input("Digite o peso do objeto (em kg): ")
        if not peso.isdigit():
            print("Você digitou um peso com valor não númerico")
            continue
        elif peso >= 30:
            print("Não aceitamos objetos tão pesados!")
            print("Entre com o peso novamente")
        else:
            peso = float(peso)
            print("O peso digitado foi de: {:.2f}kg" .format(peso))
#Fim da função pesoObjeto()

#Inicio da função rotaObjeto()
def rotaObjeto():
    print("-----Rota do Objeto-----")
    while True:
        print("Selecione a Rota:")
        print("PRSP - De Paraná para São Paulo ")
        print("SPPR - De São Paulo para Paraná ")
        print("PRSC - De Paraná para Santa Catarina ")
        print("SCPR - De Santa Catarina para Paraná ")
        rota = input()
        rota = rota.upper()
        if rota != "PRSP" and rota != "SPPR" and rota != "PRSC" and rota != "SCPR":
            print("Você digitou uma rota que não existe!")
            print("Por favor entre com a rota desejada novamente")
            continue
        else:
            break
#Fim da função rotaObjeto()


#inicio do Main
#Identificador pessoal
print("Bem Vindo a Companhia Logistica Marlos Augusto da Costa S.A")
dimensoesObjeto()