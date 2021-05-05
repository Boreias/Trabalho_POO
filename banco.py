from ficha_bancaria import *

class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__ultima_conta_criada = 0
        self.__fichario = {}
        
    def abre_conta(self, nome_cliente, cpf_cliente):
        ''' Abre uma nova conta no banco '''
        
        self.__ultima_conta_criada += 1
        
        ficha = FichaBancaria()
        ficha.set_numero(self.__ultima_conta_criada)
        ficha.set_nome(nome_cliente)
        ficha.set_cpf(cpf_cliente)
        self.__fichario[ficha.get_cpf()] = ficha
        return self.__ultima_conta_criada
  
    def deposito(self, cpf, valor):
        ''' Realiza um depósito numa conta '''
        
        if cpf in self.__fichario:
            self.__fichario[cpf].credite(valor)
            return True
        else:
            return False
            
    def saque(self, cpf, valor):
        ''' Realiza um saque numa conta '''
        
        if cpf in self.__fichario:
            self.__fichario[cpf].debite(valor)
            return True
        else:
            return False
    
    def transferencia(self, cpf_origem, cpf_destino, valor):
        ''' Realiza transferência entre duas contas '''
        
        if cpf_origem in self.__fichario and cpf_destino in self.__fichario:
            self.__fichario[cpf_destino].credite(valor)
            self.__fichario[cpf_origem].debite(valor)
            return True
        else:
            return False

    def saldo(self, cpf):       
        ''' Obtém o saldo de uma conta '''
        
        return self.__fichario[cpf].get_saldo()
 
    def encerra_conta(self, cpf):
        ''' Encerra uma conta '''
        
        if cpf in self.__fichario and self.__fichario[cpf].get_saldo() == 0:
            del self.__fichario[cpf]
            return True
        else:
            return False
        
    def conta_maior_saldo(self):
        '''Obtém o nº da conta do cliente com maior saldo'''
        
        maior_saldo = -math.inf
        nct = 0
        for ficha in self.__fichario.values():
            if ficha.get_saldo() > maior_saldo:
                maior_saldo = ficha.get_saldo()
                nct = ficha.get_numero()
        return nct

    def saldo_medio(self):
        '''Cálcula o saldo médio dos correntistas'''

        media = 0
        for ficha in self.__fichario.values():
            media += ficha.get_saldo()
        media /= len(self.__fichario)
        
        return media

    def cpfs_e_valores(self):
        lista = []
        for i in self.__fichario.values():
            lista.append([str(i.get_cpf()), str(i.get_saldo())])
        lista.sort()
        for i in range(len(lista)):
            print(' '.join(lista[i]))
    
    '''
    def cpfs_duplicados(self):
        # Obtém os cpfs duplicados (em mais de uma conta)

        lista_cpfs = []
        tupla_cpfs_duplicados = set()
        for i in range(len(self.__fichario)):
            if i.get_cpf() in lista_cpfs:
                tupla_cpfs_duplicados.add(i.get_cpf())
            else:
                lista.cpfs.append(i.get_cpf())
        
        return tupla_cpfs_duplicados
    '''
