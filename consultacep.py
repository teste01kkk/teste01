import requests
def main():
print('------𝑋.𝑋.𝑋-ꪶ͢𝐺𝑅𝐼𝑵𝐺𝛩ꫂ🇦🇱-------')
print('####################')
print('####consulta cep####')
print('####################')

cep_input = input('digite o cep que deseja consulta: ')

if len(cep_input) != 8:
   print('quantidade de digitos invalida')
exit()

requests = requests.get('https://viacep.com.br/ws/{}/json'.format(cep_input))

address_data = requests.json()
if 'erro' not in address_data:
 print('===>cep encontrado<===')
print('CEP: {}'.format(address_data['cep']))
print('lougradora {}'.format(address_data['lougradora']))
print('bairro {}'.format(address_data['bairro']))
print('cidade: {}'.format(address_data['localidade']))
print('Estado: {}'.format(address_data['uf']))

else:
	   print('{}: cep invalido....'.format(cep_input))

print(=========================)
option = int(input('deseja realiza outra consulta?/n1. sim/n2. sair/n'))
if option  -- 1:
	main()
else:
	   print('saindo....')
	   
if __name__ == '___main___' :
      main()