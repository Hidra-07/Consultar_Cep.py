import requests

class infos_cep():
	def __init__(self, cep=0):
		self.cep = cep
		self.infos_json = ''

	def capturar_infos(self):
		'''-Esse Metodo ira captura infos atraves de um Cep '''
		if self.cep == 0 and self.cep > 8: 
			print('ERROR: Cep deve ter 8 Digitos!  ')
			return 0

		r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
		
		print(r.json())
		
		self.infos_json = r.json()
	

	def exibir_infos(self):
		'''-Esse metodo exibir as infos de um modo mais organizado '''

		infos_exibida = self.infos_json
		
		for key, value in infos_exibida.items():
			print(f'{key}: {value}')
	
	
	def descobrir_cep(self, uf, cidade, longradouro):
		'''-Esse metodo descobrir o Cep atraves dos parametros passado, UF, Cidade, Longradouro'''

		r = requests.get(f'https://viacep.com.br/ws/{uf}/{cidade}/{longradouro}/json/')
		self.infos_json = r.json()[0]

		self.cep = self.infos_json['cep']

		print(f'As infos passadas retorna seguinte Cep: {self.cep} ')

'''
para fazer consultar e paga infos do Cep

cep = infos_cep(cep_a_ser_consultado)
cep.capturar_infos()
cep.exibir_infos()

'''

'''
Para descobrir um cep

cep = infos_cep()
cep.descobrir_cep('UF', 'Cidade', 'Longradouro')
cep.exibir_infos()
'''