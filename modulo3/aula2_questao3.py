idade = int(input("Digite sua idade: "))
jogou = input("Já jogou pelo menos 3 jogos de tabuleiro? ") == "True"
vitorias = int(input("Quantos jogos já venceu? "))

print("Apto para ingressar no clube de jogos de tabuleiro:", idade >= 16 and idade <= 18 and jogou and vitorias >= 1)