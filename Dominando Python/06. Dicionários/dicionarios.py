# Declarando dicionários
pessoa = {"nome": "Pedro", "idade": 17} # Primeiro método
pessoa2 = dict(nome="Guilherme", idade=19) # Segundo método
pessoa["Telefone"] = "4572 9876" # Adicionando 

print(pessoa)
print(pessoa["nome"]) # Acessando dados


contatos = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "9283-4324"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "5683-7324"},
    "ana@gmail.com": {"nome": "Ana", "telefone": "8883-4324"}
}

print(contatos["pedro@gmail.com"]["telefone"])

for chave in contatos:
    print(chave, contatos[chave])