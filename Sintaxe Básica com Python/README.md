
# Sistema Bancário - KatsBank (Primeira Versão)

## Descrição
Este é o **primeiro protótipo** do sistema bancário desenvolvido para o banco KatsBank. O sistema foi implementado com o objetivo de modernizar as operações bancárias utilizando Python. Ele inclui funcionalidades básicas para gerenciar uma conta bancária, como depósito, saque e extrato.

---

## Requisitos
- Funcionalidades disponíveis nesta versão:
  - **Depósito:** Permite adicionar valores positivos à conta.
  - **Saque:** O valor deve ser positivo, respeitar o limite de R$500.00 por operação e o saldo disponível. São permitidos até 3 saques diários.
  - **Extrato:** Exibe todas as transações realizadas e o saldo atual.
- Saldo inicial da conta: **R$1000.00**.
- As operações atualizam o saldo da conta em tempo real.

### Observação:
Esta versão é limitada a operações básicas e não inclui controle de múltiplas contas ou funcionalidades adicionais como transferências.

---

## Constantes
- `saldo`: Saldo inicial definido como **R$1000.00**.
- `extrato`: Lista que armazena todas as transações realizadas.
- `saques_diarios`: Contador de saques realizados no dia, com limite de 3 por dia.
- `SAQUES_DIARIOS_MAX`: Número máximo de saques diários permitido (fixado em **3**).
- `LIMITE_SAQUE`: Valor máximo permitido por saque (fixado em **R$500.00**).

---

## Estrutura do Menu
```plaintext
Bem-vindo ao banco KatsBank. Escolha uma das opções:
1. Depositar
2. Sacar
3. Extrato
4. Sair
```

---

## Detalhes das Funções

### 1. `deposito()`
- Realiza um depósito na conta, atualiza o saldo e registra a transação no extrato.
- **Entradas:** Valor do depósito, que deve ser um número positivo.
- **Saída:** Mensagem indicando o valor depositado e o saldo atualizado.

#### Exemplo de Mensagem:
```plaintext
Você depositou R$200.00. Seu saldo atual é R$1200.00
```

---

### 2. `saque()`
- Permite realizar um saque com as seguintes condições:
  - O valor deve ser maior que zero.
  - O valor não pode ultrapassar **R$ 500.00** por operação.
  - O saldo deve ser suficiente para a operação.
  - São permitidos até **3 saques diários**.
- **Entradas:** Valor do saque.
- **Saída:** Mensagem indicando o valor sacado e o saldo atualizado.

#### Exemplo de Mensagem:
```plaintext
Você sacou R$300.00. Seu saldo atual é R$700.00
```

---

### 3. `extrato_usuario()`
- Exibe o histórico de todas as transações (depósitos e saques) realizadas, bem como o saldo atual.
- **Entradas:** Nenhuma.
- **Saída:** Lista as transações e exibe o saldo atual.

#### Exemplo de Mensagem:
```plaintext
=== Extrato ===
- Depósito: R$100.00
- Saque: R$300.00
=================
Seu saldo atual é R$700.00
```
Caso nenhuma transação tenha sido realizada, exibe a mensagem:
```plaintext
Nenhuma transação realizada.
```

---

## Lógica Principal
- O programa exibe um menu repetitivo que permite ao usuário realizar operações até que escolha a opção **"Sair"**.
- As opções do menu são tratadas com a estrutura `match/case` (disponível a partir do Python 3.10). Se estiver usando Python em versões anteriores, utilize `if/elif/else`.

### Exemplo de Fluxo:
```plaintext
Bem-vindo ao banco KatsBank. Escolha uma das opções:
1. Depositar
2. Sacar
3. Extrato
4. Sair

Escolha uma opção: 1
Digite o valor que deseja depositar: 100
Você depositou R$100.00. Seu saldo atual é R$1100.00

Escolha uma opção: 3
=== Extrato ===
- Depósito: R$100.00
=================
Seu saldo atual é R$1100.00

Escolha uma opção: 4
Saindo do sistema...
Obrigado por usar o KatsBank!
```

---

## Observações
1. **Primeira Versão:** Este é o protótipo inicial do sistema bancário, limitado a funcionalidades básicas.
2. **Mensagens de Saída:** Todas as operações exibem mensagens claras para o usuário.
3. **Tratamento de Erros:** Validações básicas foram adicionadas para evitar entradas inválidas.