from banco import Banco

bc = Banco("Banco do Ribeirão", 999)

try:
    while True:
        entrada = input().split()
        if entrada[0] == 'abre_conta':
            bc.abre_conta(entrada[2], int(entrada[1]))
        elif entrada[0] == 'deposito':
            bc.deposito(int(entrada[1]), float(entrada[2]))
        elif entrada[0] == 'saque':
            bc.saque(int(entrada[1]), float(entrada[2]))
        elif entrada[0] == 'transferencia':
            bc.transferencia(int(entrada[1]), int(entrada[2]), float(entrada[3]))

except:
    bc.cpfs_e_valores()

'''        
nj = bc.abre_conta("Joãozinho", 23456)
nm = bc.abre_conta("Mariazinha", 123456)

bc.deposito(nj, 100)
bc.deposito(nm, 250)
bc.saque(nj, 50)
bc.transferencia(nm, nj, 20)

print(bc.saldo(nj))
print(bc.saldo(nm))
'''
