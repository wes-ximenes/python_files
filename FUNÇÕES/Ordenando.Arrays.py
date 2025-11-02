
#função para percorrer um array e sinalizar o menor, um por vez.
def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

#função para criar um novo array e armazenar um por um, ordenando em crescente, usando a função anterior.
def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range (len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor)) #pop() comando que remove o valor da lista original, e retorna ele para a nova lista(novoArr).
    return novoArr




print (ordenacaoporSelecao([3,6,4,9,18,15,2]))    