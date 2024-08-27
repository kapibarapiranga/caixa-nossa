#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:44:41 2024

@author: Kapibara Pirãga
"""
from datetime import date

# VARIÁVEIS E CONSTANTES
LIMITE_SAQUE = 500
LIMITE_NUM_SAQUES = 3
BOAS_VINDAS = "\n\n\nSeja Bem-Vindo ao Terminal do Banco Nosso S.A."
ERRO = " operação inválida "
                         
saldo = 0
extrato = []
num_saques = 0

menu_msg = """
Selecione a Opção Desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# FUNÇÔES
def menu():
    while True:
        print(BOAS_VINDAS)
        opcao = input(menu_msg)
        
        if opcao == "d":
            print("Depósito")
            deposito_valor = float(input("Digite o valor que deseja depositar: "))
            deposito(deposito_valor)
        
        elif opcao == "s":
            print("Sacar")
        
        elif opcao == "e":
            print("Extrato")
        
        elif opcao == "q":
            print("Sair")
            break
        
        else:
            print(ERRO.upper().center(47, "="))


def deposito(valor):
    global saldo 
    saldo += valor
    
    data = date.today()
    extrato.append([data, valor, saldo])
    print(extrato)
    
        
        
        

# LOGOTIPO DO BANCO
logo = '''
----------------------------------------++++++-------+++++------------------------------------------
------------------------------------+++---------------------+++-------------------------------------
---------------------------------++-----------++-++------------+++----------------------------------
-------------------------------++------+---+--+--+-++++-+---------++--------------------------------
-----------------------------++-----++-++---------------++-+++-------+------------------------------
---------------------------++------+-+------------------------++++----++----------------------------
--------------------------+------++---------++++++++++++--------+--+----++--------------------------
-------------------------+----+-+-------+++--------------++-------++------+-------------------------
------------------------+-------------++--------------------++-------------+------------------------
-----------------------+------------+-------------------------++------------+-----------------------
-----------------------++++++++++++------------------------------+++++++++++++----------------------
------------------------++++-+++-----++++++++--+++++++++++++-+++++----+++++++-----------------------
---------------------++##+#+-+###+----++##++---+#+##+-++###+-++#++----+####+------------------------
--------------------+####++----##+---+-+###+----####+--+###+++#+-----+-+###+------------------------
--------------------#####+-----++----#++###+----####+---++##+++------++-+###+-----------------------
-------------------+####++----------+#+-+###+---####+-----+###------+#+-+###+-----------------------
-------------------+#+##+-----------+++-+##++---####+----+++#++-----+#+-+####+----------------------
--------------------+#+##+------++-+#++##+###+--##+#+--++#+++##++--+#++######+----------------------
---------------------+###++---++#+++++---+###+++#+##+-+##+--+####++##+---+###++---------------------
-----------------------++##+++#+++####-+##################++##########+-+######+--------------------
----------------------------------------------------------------------------------------------------
-----------------------++++++++++++-----------------------------++++++++++++++----------------------
-----------------------+------------++------------------------++------------+-----------------------
------------------------+------++-----++--------------------++-------+-----+------------------------
-------------------------+-----++++------++--------------++------+-------++-------------------------
--------------------------+-------+----------++++++++++----------+------++--------------------------
---------------------------++------++-+--------------------+++++------++----------------------------
-----------------------------++-------+--+---------------+-+--------++------------------------------
-------------------------------++-----------+-++--++-+++++--------++--------------------------------
---------------------------------+++---------------------------++-----------------------------------
------------------------------------+++--------------------+++--------------------------------------
-----------------------------------------++++++----+++++++------------------------------------------
'''

print(logo)

menu()

