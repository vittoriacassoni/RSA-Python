from cripto import RSA

msg = 'The information security is of significant importance to ensure the privacy of communications'

print('-------------------------------------------------------------------------------------------------------')
print('Bruna Cristina Torres')
print('Laura Alves Ferreira')
print('Mariana Carnevale de Lima')
print('Vittoria Cassoni')
print('-------------------------------------------------------------------------------------------------------')

rsa = RSA.gera_chaves();

rsa.mostra_valores();

valoresCripto = rsa.criptografa(msg)

print('Frase original: {}'.format(msg))
print('-------------------------------------------------------------------------------------------------------')

print('Frase criptografada: {}'.format(valoresCripto))
print('-------------------------------------------------------------------------------------------------------')
print('Frase descriptografada: {}'.format(rsa.decriptografa(valoresCripto)))
