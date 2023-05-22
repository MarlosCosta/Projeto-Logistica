#Atividade 03 de 04 do Trabalho
#Inicio da função obter_dimensoes_objeto()
def obter_dimensoes_objeto():
    print("-----Cadastro das Dimensões do Objeto-----")
    while True:
        #Tratativa do erro caso usuario entre com valor não numerico
        try:
            altura = float(input("Digite o altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
        except ValueError:
            print("Você digitou alguma dimensão do objeto com valor não numérico!")
            print("Digite as dimensões novamente")
            continue

        # Verifica se algum valor é menor que zero
        if altura <= 0 or comprimento <= 0 or largura <= 0:
            print("Você digitou alguma dimensão do objeto com valor igual ou abaixo de zero!")
            continue

        # Cálculo do volume
        volume_objeto = altura * comprimento * largura
        print("O volume do objeto é (em cm³) : {:.2f}" .format(volume_objeto))

        #calcula o valor do objeto de acordo com o volume apresentado
        if volume_objeto < 1000:
            valor_objeto = 10
        elif volume_objeto < 10000:
            valor_objeto = 20
        elif volume_objeto < 30000:
            valor_objeto = 30
        elif volume_objeto < 100000:
            valor_objeto = 50
        else:
            print("Não aceitamos objeto com dimensões tão grandes")
            continue

        break

    #Retorna a variavel para ser usada fora da função
    return valor_objeto
#Fim da função obter_dimensoes_objeto()
#Inicio da função obter_peso_objeto()
def obter_peso_objeto():
    print()#Pula uma linha para que a saida no console fique mais legivel
    print("-----Cadastro do Peso do Objeto-----")
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
        except ValueError:
            print("Você digitou o peso do objeto com valor não numérico!")
            print("Digite o peso novamente")
            continue

        if peso <= 0:
            print("Você digitou o peso menor/igual a zero!")
            print("Digite o peso novamente")
            continue

        #calcula o multiplicador com base no peso digitado
        if peso <= 0.1:
            multiplicador_peso  = 1
        elif peso < 1:
            multiplicador_peso  = 1.5
        elif peso < 10:
            multiplicador_peso  = 2
        elif peso < 30:
            multiplicador_peso  = 3
        else:
            print("Não aceitamos objetos tão pesados!")
            print("Entre com o peso novamente")
            continue

        break

    return multiplicador_peso #Retorna a variavel para ser usada fora da função

    print("O peso digitado foi de: {:.2f}kg".format(peso))
#Fim da função obter_peso_objeto()

#Inicio da função obter_rota_objeto()
def obter_rota_objeto():
    print()#Pula uma linha para que a saida no console fique mais legivel
    print("-----Seleção da Rota do Objeto-----")
    while True:
        print("Rotas disponiveis:")
        print("PRSP - De Paraná para São Paulo ")
        print("SPPR - De São Paulo para Paraná ")
        print("PRSC - De Paraná para Santa Catarina ")
        print("SCPR - De Santa Catarina para Paraná ")
        rota = input("Digite a rota desejada (PRSP/SPPR/PRSC/SCPR): ")
        rota = rota.upper() #permite letra maiuscula ou minuscula

        #Calcula o multiplicador com base na rota selecionada
        if rota == "PRSC":
           multiplicador_rota = 1
        elif rota == "SCPR":
            multiplicador_rota = 1
        elif rota == "PRSP":
            multiplicador_rota = 1.5
        elif rota == "SPPR":
            multiplicador_rota = 1.5
        else:
            print("Você digitou uma rota que não existe!")
            print("Por favor entre com a rota desejada novamente")
            continue

        break

    return multiplicador_rota #Retorna a variavel para ser usada fora da função
#Fim da função obter_rota_objeto()


#inicio do Main
#Identificador pessoal
print("Bem Vindo a Companhia Logistica Marlos Augusto da Costa S.A")

#Recebe a variavel de retorno da função e aplica na variavel de mesmo nome fora da função
valor_objeto = obter_dimensoes_objeto()
multiplicador_peso = obter_peso_objeto()
multiplicador_rota = obter_rota_objeto()

#Variavel criada para calcular o valor final e apresentar o resultado com base nos dados fornecidos pelo usuario
valor_final = valor_objeto * multiplicador_peso * multiplicador_rota
print()
print("O valor final é de: R${:.2f} (dimensões: R${} * peso: {} * rota: {}" .format(valor_final, valor_objeto, multiplicador_peso, multiplicador_rota))