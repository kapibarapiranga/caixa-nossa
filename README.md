# Banco Caixa Nossa
Exercício de criação de um sistema bancário simples.

Projeto realizado para entrega no curso **Criando um Sistema Bancário com Python** da DIO, disponível em:
[Criando um Sistema Bancário com Python](https://web.dio.me/lab/desafio-de-projeto-criando-um-sistema-bancario/).

Abaixo uma pequena referência à Caixa Econômica do Estado de São Paulo que será singelamente homenageada no presente projeto.

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▒░░░░▒░░░░░░░▒▒▒░░▒░░░░░░░░░░░░░░
░░░░░░░░░░░░▒░░▒░░░░▒▒░░▒▒░░░░░░░▒░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░░░░░░░░░▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░░░
░░░░░░░░░▒▓▓▒░▓▒░░▓▓░░▓█░▒▓▒▒▓░░▒█▓░░░░░░░░░░░
░░░░░░░░░█▓▓░░░░░▓▓▓▒░▓▓░░▒▓▒░░▒▓▓▓▒░░░░░░░░░░
░░░░░░░░░█▓▓░░░▒▓▓█▓▓░▓▓░░▓▓▓▒░▓▓█▓▓░░░░░░░░░░
░░░░░░░░░░▒▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓▓▒▓▓▓▓▒▒▓▓▒░░░░░░░░░
░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░░░
░░░░░░░░░░░▒░░▒░░░▒░░░░░░░░▒░░░░░░▒░░░░░░░░░░░
░░░░░░░░░░░░▒░░░▒░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒░░░░░▒▒░▒▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▒░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

## Proposta
DESAFIO:
Fomos contrataos por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e par isso escolheu a linguagem Python <img height="25px" src="https://skillicons.dev/icons?i=python" />. Para a primeira versão do sistema devemos implementar apenas 3 operações:
- Depósito
- Saque
- Extrato

#### Depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário. dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

#### Saque
O sitema deve permitir 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#### Extrato
Esta operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.4 = R$ 1500.40
