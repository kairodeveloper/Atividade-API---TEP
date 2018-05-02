import requests, os


API_LOCAIS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"
API_NOMES_ID_LOCALIDADE_URL = "http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?localidade="


RELACAO_DE_ESTADOS_CACHE = requests.get(API_LOCAIS_URL+"/estados").json()


def main():
	mostarInformacaoDaUF()

def mostarInformacaoDaUF():
	while True:
		UF = {}
		entrada = input("insira o nome ou UF do Estado, 0 sair-> ")
		if entrada == "0":
			break
		try:
			UF = getCodigoDoEstadoPeloNome(entrada)
		except:
			print ("Estado não encontrado")
			break
		
		print("\n\n    Dados da Unidade Federativa\n\n  nome: .................. %s\n  sigla: ................. %s\n  região: ................ %s\n  numero de municipios: .. %s" %(UF['nome'], UF['sigla'], UF['regiao']['nome'],len(getRelacaoDeMunicipiosDoEstado(UF))))
		print ("\n     Ranking de Nomes Mais Populares no Estado\n")
		for nome in getTopNomesByIDLocal(UF):
			print ("%s - %s - %s ocorrências"%(nome['ranking'], nome['nome'], nome['frequencia']))
		print()

		municipios = input("deseja listar os municipios? (s/n)")
		if municipios.upper() == "S":
			for municipio in getRelacaoDeMunicipiosDoEstado(UF):
				print (municipio['nome'])

def getCodigoDoEstadoPeloNome(nome):
	for dado in RELACAO_DE_ESTADOS_CACHE:
		if dado['sigla'].upper() == nome.upper() or dado["nome"].upper() == nome.upper():
			return(dado)

def getRelacaoDeMunicipiosDoEstado(UF):
	todos_municipios = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios/").json()
	municipios = []
	for municipio in todos_municipios:
		if municipio['microrregiao']['mesorregiao']['UF']['id'] == UF['id']:
			municipios.append(municipio)
	return municipios

def getTopNomesByIDLocal(UF, limit=10):
	nomes = requests.get(API_NOMES_ID_LOCALIDADE_URL+str(UF['id'])).json()
	return(nomes[0]['res'][0:limit])

if __name__ == '__main__':
	main()