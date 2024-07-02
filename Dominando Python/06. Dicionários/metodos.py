contatos = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "9283-4324"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "5683-7324"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "8883-4324"}
}

contatos.clear()
print(contatos)

print(dict.fromkeys(["nome"]))
print(dict.fromkeys(["nome"], "Julia"))

print(contatos.get("joao@gmail.com", {}))

contatos.items() # Lista de tuplas

numeros = {"telefone": "399", "celular": "7889 5646"}
print(numeros.keys())
