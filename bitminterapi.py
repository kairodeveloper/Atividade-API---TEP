import requests, time

api_url = "https://bitminter.com/api/pool/"

def main():

	while True:
		op = input(" 1 - dados gerais\n 2 - dados detalhados\n 0 - sair\n---> ")

		if op == "0":
			break
		elif op == "1":
			getGeneralMininglData(int(input("intervalo de atualização (s): ")))
		elif op == "2":
			getDetailedMiningData(int(input("intervalo de atualização (s): ")))
	

def getGeneralMininglData(refresh):

	print ("Obtendo dados de bitminter.com...")
	while True:
		print("\n%s %s %s"% (20*"#", time.strftime("%a, %d %b %Y %H:%M:%S ", time.gmtime()), "#"*20))

		dados = requests.get(api_url+"stats").json()
		
		print("\n   Informações Gerais ")

		print (" Taxa De Hash (GH/s): %s" %dados['hash_rate'])
		print (" Mineradores Online: %s" %dados['active_workers'])
		print (" Usuários Online: %s" %dados['active_users'])
		time.sleep(refresh)


def getDetailedMiningData(refresh):

	print ("Obtendo dados de bitminter.com...")
	while True:
		dados = requests.get(api_url+"round").json()

		print("\n%s %s %s"% (20*"#", time.strftime("%a, %d %b %Y %H:%M:%S ", time.gmtime()), "#"*20))
		
		print("\n   Informações Gerais ")

		print (" Taxa De Hash (TH/s): %.2f" %(float(dados['hash_rate'])/1024))
		print (" Mineradores Online: %s" %dados['active_workers'])
		print (" Usuários Online: %s" %dados['active_users'])

		CHAINS = dados['chains']
		BITCOIN = CHAINS['BTC']
		NAMECOIN = CHAINS['NMC']

		print (" \n Informações Específicas \n")
		print ("          BITCOIN\n   Aceitas:     %s\n   Rejeitadas:  %s\n   Duração:     %s\n   Dificuldade: %s\n"%(BITCOIN['accepted'], BITCOIN['rejected'], BITCOIN['duration'], BITCOIN['difficulty']))
		print ("          NAMECOIN\n   Aceitas:     %s\n   Rejeitadas:  %s\n   Duração:     %s\n   Dificuldade: %s"%(NAMECOIN['accepted'], NAMECOIN['rejected'], NAMECOIN['duration'], NAMECOIN['difficulty']))
		time.sleep(refresh)

if __name__ == '__main__':
	main()

