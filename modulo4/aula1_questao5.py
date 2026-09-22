n = int(input("Digite a quantidade de respondentes: "))

soma = 0

for i in range(n):
    idade = int(input("Digite a idade: "))
    soma += idade

media = soma / n

print(f"Média das idades: {media:.2f}")