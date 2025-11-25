# dicionário representando uma biografia simples
eu = {
    "nome": "Wesley",
    "idade": 27,
    "cidade": "Recife",
    "genero": "Masculino"
}

eu["altura"] = 1.74 # Adicionando novas chave-valor ao dicionário
eu["profissao"] = "Desenvolvedor"

eu.update({"profissao": "Programador"}) # Atualizando valor existente utilizando update(), dá pra atualizar múltiplos valores ao mesmo tempo.

#Dentro de um dicionário, podemos ter outros dicionários e listas como valores.
eu["habilidades"] = {"programacao": ["Python", "Mysql", "C"], "idiomas": ["Português", "Inglês"]}

print(eu)
