# RSA

BIT_SIZE = 2048
class RSA:

    @staticmethod
    def eh_primo(n):
        return eh_primo(n)
    
    def __init__(self, p, q, e=None):
        self.p = p #numero primo
        self.q = q #numero primo

        #calculo de n
        self.n = p*q
        #calculo do totiente
        self.totient_n = calc_lcm(p-1, q-1)
        #escolha do e
        if e is None:
            self.e = calcula_e(self.totient_n)
        else:
            self.e = e

        #calculo do d, inverso multiplicativo do e            
        self.d = inverso_multiplicativo(self.e, self.totient_n)

    def criptografa_char(self, char):
        return pow(char, self.e, self.n)

    def descriptografa_valor(self, valor):
        return pow(valor, self.d, self.n) 

    def criptografa(self, palavra):
        palavra_criptografa = []
        for char in palavra:
            codigo_char = ord(char)
            criptografia_char = self.criptografa_char(codigo_char)
            
            palavra_criptografa.append(criptografia_char)
        
        return palavra_criptografa

    def decriptografa(self, valores):
        palavra_descriptografada = ''
        for n in valores:

            codigo_char_descriptografado = self.descriptografa_valor(n)
            
            valor_char = chr(codigo_char_descriptografado)
            palavra_descriptografada += valor_char
        
        return palavra_descriptografada

    @staticmethod
    def gera_chaves():
        p, q = gera_numero_primo(BIT_SIZE), gera_numero_primo(BIT_SIZE)
        return RSA(p, q)

    def mostra_valores(self):
        print('------------------------------------------------------------')
        print('VALORES USADOS NO RSA:')
        print('------------------------------------------------------------')
        print('P = ', self.p)
        print('Q = ', self.q)
        print('N = ', self.n)
        print('TOTIENTE DE N = ', self.totient_n)
        print('E = ', self.e)
        print('D = ', self.d)
        print('P em bits = ', pega_bits(self.p))
        print('Q em bits = ', pega_bits(self.q))
        print('N em bits = ', pega_bits(self.n))
        print('------------------------------------------------------------')


# PRIMOS ---------------------------------------------------------------------------------------------------

import random as _r
import time as _t
_r.seed(_r.random())

def eh_primo(n, k=64):

    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    if n < 100000:
        with open('primos.txt') as f:
            conteudo = f.readlines()
            primos = [int(x.strip()) for x in conteudo] 
            return n in primos
    else:
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2

        for _ in range(k):
            a = _r.randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

def gera_primos(tamanho):

    p = _r.getrandbits(tamanho)
    
    p |= (1 << tamanho - 1) | 1

    return p
    
def gera_numero_primo(tamanho=1024):
  
    p = 4

    while not eh_primo(p, 128):
        p = gera_primos(tamanho)
    return p

# HELPER (FUNCOES GERAIS) ----------------------------------------------------------------------------------

import random as _r
import math as _m

def pega_bits(x):
	return len(bin(abs(x))[2:])

def sao_coprimos_recursivo(x, y):
    return sao_coprimos(x, y)
    
def sao_coprimos(x, y):
    return _calc_gcd(x, y) == 1

def _calc_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def calc_lcm(x, y):
   lcm = (x*y)//_calc_gcd(x, y)
   return lcm

def calcula_e(totient):
    tamanho_maximo_bits = _r.randint(2, pega_bits(totient)-1)

    tamanho_maximo_bits = min(75, tamanho_maximo_bits)

    e = gera_numero_primo(tamanho_maximo_bits)
    
    while not sao_coprimos(e, totient):
        e = gera_numero_primo(tamanho_maximo_bits)

    return e

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def inverso_multiplicativo(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Não é possivel calcular o inverso multiplicativo')
    return x%m