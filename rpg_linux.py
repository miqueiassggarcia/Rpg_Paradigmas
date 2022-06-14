import crypt
from random import randint
import time

items = [
    [2, False, "chave", False, False],
    [3, False, "machado", False],
    [7, False, "gasolina", False]
]

valoresLocais = [0, 0]

pessoa = False
casa = False
portaSotao = False
password = "dlkSaElieQle6"

mapaLocais = [
    [
        "Você volta para o inicio, onde tudo começou",
        "Você percebe que há apenas algumas trilhas uma há direita, outra em frente, outra a esquerda e uma nas costas",
        "Você volta para o inicio, onde tudo começou, mas ainda com uma sensação estranha"
    ],
    [
        "Você encontra um carro abandonado, ele não parece ter sido usado a muito tempo",
        "Ele está com a chave na ignição, você tenta ligar, mas ele não liga, parece estar com o tanque vazio",
    ],
    [
        "Você encontra uma pessoa que parece estar ferida no chão da floresta, a única coisa que ela consegue lhe falar"
        "\né 'Não há tempo, ele está na floresta', e então ela desmaia",
        "Você percebe que algo parecido com uma chave está caindo do bolso da pessoa",
        "Você volta e a pessoa não acordou, você não sabe dizer se ela está morta ou não"
    ],
    [
        "Você encontra uma parte da floresta desmatada, parece com um local de coleta de madeira",
        "Você encontra um machado perto de um tronco e madeira que parece ter sido golpeado múltiplas vezes,"
        "\nprovavelmente para corte de madeiras"
    ],
    [
        "Você encontra uma casa de madeira não muito grande",
        "A porta está fechada, mas ela não parece ser tão resistente",
        "Mesmo que a porta seja fraca, você é mais",
    ],
    [
        "Você entra na casa, é um lugar pequeno, a cozinha suja lhe chama atenção, há uma faça perto de uma chaira com"
        "\nsangue seco",
        "Você vasculha a casa e encontra uma escada para um sótão"
    ],
    [
        "Você desce a escada e encontra uma porta, ela está fechada com um cadeado de senha, são necessários 5 números",
        "Você encontra um baú embaixo das escadas que dão no sótão, ele está trancado, é necessário uma chave",
        "Você abre o baú e encontra algumas roupas velhas em meio a ferramentas, mas um papel chama sua atenção, nele"
        "\nhá escrito:"
        "\n d o  n   t    l   o   o   k   _ _ _ _"
        "\n ⇩ ⇩  ⇩   ⇩    ⇩   ⇩   ⇩   ⇩"
        "\n 7 18 17  23   15  18  18  14\n",
        "Você volta do sótão, com um sentimento estranho de que tinha alguém lhe observando, enquanto olha para a"
        "\nescada que peva a parte de cima da casa"
    ],
    [
        "Você entra no sótão, e tudo que encontra é uma pequena sala que fede a podre, com muito entulho acumulado e"
        "\nsacos plásticos que parecem ter algo podre dentro",
        "Você nota que há algo parecido com um galão de gasolina"
    ],
    [
        "Você liga o carro e finalmente você consegue sair desse lugar estranho e horrível que você estava",
        "Você acelera o carro com esperança de encontrar um lugar seguro para se abrigar",
        "Uma silhueta estranha saindo da floresta e se poe no caminho com um machado",
        "Você estava muito rápido e tenta desviar",
        "Você perde o controle e bate o carro em uma arvore, o impacto lhe faz bater a cabeça e começar a sangrar",
        "Você tenta ligar o carro novamente, ele liga mas logo falha",
        "Você sai pra fora e percebe que o tanque estava vazando gasolina, ele está sem gasolina de novo",
        "Você entra na floresta com esperança de encontrar alguém pra lhe ajudar, mas o sangramento lhe faz desmaiar",
        "Você acorda com um barulho de alguém chegando. Percebendo que é uma pessoa diferente, você avisa",
        "'Não há tempo, ele está na floresta', mas você está muito fraco, e então, desmaia"
    ]
]


def testarSeExiste(frase, palavraAPesquisar):
    frase = frase.lower().split()

    for palavra in palavraAPesquisar:
        palavra.lower()

    for palavra in frase:
        if palavra in palavraAPesquisar:
            return True
    return False


def testarSeExisteItem(frase, palavraAPesquisar):
    frase = frase.lower().split()

    for palavra in palavraAPesquisar:
        palavra.lower()

    for palavra in frase:
        if palavra in palavraAPesquisar:
            if palavra == items[0][2]:
                if items[0][1]:
                    if items[0][3]:
                        print("\nA chave está no seu bolso")
                        return False
                    items[0][3] = True
                    return True
            if palavra == items[1][2]:
                if items[1][1]:
                    if items[1][3]:
                        print("\nO machado já está na sua mão")
                        return False
                    items[1][3] = True
                    return True
            if palavra == items[2][2]:
                if items[2][1]:
                    if items[2][3]:
                        print("\nVocê já está levando o galão")
                        return False
                    items[2][3] = True
                    return True
    return False


def tresPontinhos():
    for i in range(2):
        time.sleep(0.8)
        print(".", end="")
    time.sleep(0.8)
    print(".")


def olharParaTras():
    print("\n"*200)
    teste = str(input("\033[1mVocê tem certeza que quer olhar para tras?\033[0m\n"))
    if testarSeExiste(teste, ["sim", "tenho", "vou"]):
        caso = randint(1, 100)
        if caso <= 20:
            print("\033[1mTem alguém atrás de você\033[0m", end="")
            tresPontinhos()

            caso = randint(1, 100)
            print("Ele tenta lhe atacar", end="")
            tresPontinhos()
            if caso <= 70:
                print("E você nao foi rapido o suficiente!")
                print("VOCE MORREU!")
                exit()
            else:
                print("Você consegue desviar e corre dele, após ter ido pra floresta e correr entre as arvores,"
                      "\nvocê consegue dispistar ele, você para e olha")
                valoresLocais[0] = randint(1, 4)
                valoresLocais[1] = 0

                return -1
        else:
            return 1
    else:
        return 0


def testarSenha(senha):
    senhaSemEspaco = senha.replace(" ", "")

    destravou = crypt.crypt(senhaSemEspaco, "dlb") == password

    return destravou


def imprimirDescricao(texto):
    print("\n", texto, end="", sep="")

    tresPontinhos()
    retorno = input("\nO que você faz agora?\n")
    return retorno


comando = imprimirDescricao("Você acorda em uma floresta, sem saber como você veio para lá,"
                            "\na lua brilha no meio do ceú")

while True:
    # items
    if testarSeExiste(comando, ["pegar"]) and testarSeExisteItem(comando, ["machado"]) and valoresLocais[0] == 3:
        # testar machado
        comando = imprimirDescricao("Você pegou o machado")
    elif testarSeExiste(comando, ["pegar"]) and testarSeExisteItem(comando, ["chave"]) and valoresLocais[0] == 2:
        # testar chave
        comando = imprimirDescricao("Você pegou a chave")
    elif testarSeExiste(comando, ["pegar"]) and testarSeExisteItem(comando, ["gasolina"]) and valoresLocais[0] == 7:
        # testar gasolina
        comando = imprimirDescricao("Você pegou o galão de gasolina")

    # checar
    elif testarSeExiste(comando, ["checar", "olhar", "verificar", "em volta", "buscar"]):  # checar ambiente
        if valoresLocais[0] == items[0][0]:
            items[0][1] = True
        elif valoresLocais[0] == items[1][0]:
            items[1][1] = True
        elif valoresLocais[0] == items[2][0]:
            items[2][1] = True
        elif valoresLocais[0] == 6:
            items[0][4] = True
        if valoresLocais[0] == 5:
            casa = True
        valoresLocais[1] = 1
        comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        valoresLocais[1] = 0

    # usar e destrancar
    elif testarSeExiste(comando, ["abrir", "arrombar"]) and testarSeExiste(comando, ["porta"])\
            and valoresLocais[0] == 4:  # abrir porta casa
        if items[1][3]:
            print("\nVocê consegue arrombar a porta com o machado")
            time.sleep(1)
            valoresLocais[0] = 5
            valoresLocais[1] = 0
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        else:
            valoresLocais[1] = 2
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    elif testarSeExiste(comando, ["abrir", "destrancar"]) and testarSeExiste(comando, ["baú"])\
            and valoresLocais[0] == 6:  # abrir baú sotão
        if items[0][3] and items[0][4]:
            time.sleep(1)
            valoresLocais[0] = 6
            valoresLocais[1] = 2
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        else:
            if items[0][4]:
                comando = imprimirDescricao("Você não consegue abrir o baú")
            else:
                comando = imprimirDescricao("A lua brilhante lhe deixa confuso, mas você para e pensa um pouco")
    elif testarSeExiste(comando, ["abrir", "destrancar"]) and testarSeExiste(comando, ["porta"])\
            and valoresLocais[0] == 6:  # abrir porta sotão
        if not portaSotao:
            valor = input("Depois de pensar você tenta a senha:\n")
            if testarSenha(valor):
                valoresLocais[0] = 7
                valoresLocais[1] = 0
                comando = imprimirDescricao("Você consegue destrancar a porta\n"
                                            ""+mapaLocais[valoresLocais[0]][valoresLocais[1]])
                portaSotao = True
            else:
                comando = imprimirDescricao("Você coloca a senha, mas nada acontece")
        else:
            valoresLocais[0] = 7
            valoresLocais[1] = 0
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    elif testarSeExiste(comando, ["ligar", "abastecer"]) and testarSeExiste(comando, ["carro"]) \
            and valoresLocais[0] == 1:  # abastecer e ligar carro
        if items[2][3]:
            print("Você abastece o carro com o galão que achou")
            print(mapaLocais[8][0], "\n")
            time.sleep(2)
            print(mapaLocais[8][1], "\n")
            time.sleep(2)
            print("Mas", end="", sep="")
            tresPontinhos()
            print()
            print(mapaLocais[8][2], end="", sep="")
            tresPontinhos()
            print()
            print(mapaLocais[8][3], end="", sep="")
            tresPontinhos()
            print()
            print(mapaLocais[8][4], end="", sep="")
            tresPontinhos()
            print()
            print(mapaLocais[8][5], "\n")
            time.sleep(2)
            print(mapaLocais[8][6], "\n")
            time.sleep(2)
            print(mapaLocais[8][7], "\n")
            time.sleep(2)
            print(mapaLocais[8][8], "\n")
            time.sleep(2)
            print(mapaLocais[8][9], "\n")
            time.sleep(2)
            exit()
        else:
            comando = imprimirDescricao("Você não possui gasolina para abastecer o carro")

    # mapa
    elif testarSeExiste(comando, ["atras", "sul", "costas", "tras"]) and valoresLocais[0] == 0:  # ir carro
        if items[2][3]:
            valor = olharParaTras()
            if valor == 0:
                comando = "padrão"
            elif valor == 1:
                valoresLocais[0] = 1
                valoresLocais[1] = 0
                comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
            elif valor == -1:
                comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        else:
            valoresLocais[0] = 1
            valoresLocais[1] = 0
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    elif testarSeExiste(comando, ["direita", "leste"]) and valoresLocais[0] == 0:  # ir pessoa
        valoresLocais[0] = 2
        if pessoa:
            valoresLocais[1] = 2
        else:
            valoresLocais[1] = 0
        comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        pessoa = True
        valoresLocais[1] = 0
    elif testarSeExiste(comando, ["frente", "adiante", "norte"]) and valoresLocais[0] == 0:  # ir desmatado
        valoresLocais[0] = 3
        valoresLocais[1] = 0
        comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    elif testarSeExiste(comando, ["esquerda", "oeste"]) and valoresLocais[0] == 0:  # ir casa
        valoresLocais[0] = 4
        valoresLocais[1] = 0
        comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    elif testarSeExiste(comando, ["sotão"]) and valoresLocais[0] == 5 and casa:  # ir sotão
        valoresLocais[0] = 6
        valoresLocais[1] = 0
        comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])

    # voltar
    elif testarSeExiste(comando, ["voltar", "retornar"]):
        if valoresLocais[0] == 7:
            valor = olharParaTras()
            if valor == 0:
                comando = "padrão"
            elif valor == 1:
                valoresLocais[0] -= 1
                valoresLocais[1] = 3
                comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
            elif valor == -1:
                comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        elif 0 < valoresLocais[0] < 5:
            valoresLocais[0] = 0
            valoresLocais[1] = 0
            if items[2][3]:
                valoresLocais[1] = 2
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        elif valoresLocais[0] > 0:
            valoresLocais[0] -= 1
            valoresLocais[1] = 0
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
        else:
            comando = imprimirDescricao(mapaLocais[valoresLocais[0]][valoresLocais[1]])
    else:
        comando = imprimirDescricao("Você tenta fazer isso, mas não chega a lugar nenhum e tenta outra coisa")
