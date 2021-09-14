# calculadora margem de lucro proporcional inverso  

custo = int(input('digite o custo do produto:'))
margem = int(input('digite a margem desejada:'))

porcentagem = margem/100
proporcional_inverso = (1 - porcentagem)

preco_final = custo/proporcional_inverso
print(preco_final)