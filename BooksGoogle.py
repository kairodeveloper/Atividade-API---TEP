import requests

titulo = input("Digite o livro que você deseja encontrar...")
request = requests.get("https://www.googleapis.com/books/v1/volumes?q=python").json()

for i in request["items"]:
    print(i["volumeInfo"]["title"])
