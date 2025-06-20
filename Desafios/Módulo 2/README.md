# Projeto - Sistema Bancário com Python e POO

Este projeto implementa um sistema bancário simples em Python com suporte a múltiplos clientes e contas, histórico de transações, saques, depósitos, e extração de extrato. É uma aplicação orientada a objetos com práticas de boas estruturas de classes, herança, abstração e encapsulamento.

---

## 🧠 Funcionalidades

- Cadastro de **clientes** (Pessoa Física)
- Criação de **contas correntes**
- Realização de **depósitos** e **saques**
- Emissão de **extratos**
- **Histórico de transações**
- **Validação de limite de saques** e de transações diárias
- Iteração sobre contas existentes

---

## Estrutura de Classes

### `Cliente` e `PessoaFisica`
- Representa o cliente do banco.
- Armazena endereço, CPF, nome e data de nascimento.

### `Conta` e `ContaCorrente`
- Gerencia saldo, saque e depósito.
- A `ContaCorrente` adiciona limites específicos como valor máximo por saque e quantidade diária de saques.

### `Transacao`, `Saque` e `Deposito`
- Classes abstrata e concretas para representar operações bancárias.

### `Historico`
- Registra todas as transações feitas por conta.
- Permite gerar relatórios filtrados e contar transações diárias.

### `ContasIterador`
- Implementa um iterador personalizado para listar as contas de forma formatada.

---

## Menu de Operações

Ao rodar o script, o usuário interage com o seguinte menu:

```
=============== MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
```

---

## Regras de Negócio

- Máximo de **10 transações por dia** por conta.
- Limite de **R$500 por saque** e **50 saques por conta**, ajustável.
- Validação de CPF antes da criação de contas ou execução de operações.

---

---

## ▶️ Como Executar

Certifique-se de ter o Python 3.8+ instalado. Para rodar o projeto:

```bash
python SistemaBancarioAtualizado.py
```

---

## 🧑‍💻 Autor

Pedro Henrique Rebechi
