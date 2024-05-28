# 28/05/2024
# ganhos e despesas em python
# @Kokai

print("Digite um dos numeros abaixo para começar, digite qualquer outro numero para finalizar")
print("______________")
print("1- Adicionar ganho\n2- Adicionar gasto")
print("______________")

# função para adicionar as informações do gasto ou do ganho
def adicionar_valor(opcao):
    titulo = input("Nome do ganho ou do gasto: ")
    valor = int(input("Valor: "))
    tipo = ""
    if opcao == 1:
        tipo = "ganho"
    else:
        tipo = "despesa"

    dados = [titulo, valor, tipo]             

    return dados

tabela = []

while True:
    dados = []
    # ler a escolha do usuario
    opcao = int(input("Digite a opção: " ))
    
    if opcao == 1:
        dados = adicionar_valor(opcao)
        tabela.append({
            "titulo": dados[0],
            "valor": dados[1],
            "tipo": dados[2]
        })
        del dados[:] 

    elif opcao == 2:
        dados = adicionar_valor(opcao)
        tabela.append({
            "titulo": dados[0],
            "valor": dados[1] * -1,
            "tipo": dados[2]
        })
        del dados[:] 

    else:
        soma = 0
        totalGanhos = 0
        totalGastos = 0
        if len(tabela) > 0:
         for item in tabela:
             soma += int(item['valor'])
             if item['tipo'] == "despesa":
                 totalGastos += 1
             else:
                 totalGanhos += 1            

        print ("Seu saldo total é de R$", soma, "O total de ganhos foram:", totalGanhos, "e o total de gastos foram:", totalGastos)
        break

