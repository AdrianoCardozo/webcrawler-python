import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"

# Os headers são para informar ao servidor que estamos acessando o site via navegador, caso ao contrário ele não deixará acessar
}

website = requests.get("https://www.tripadvisor.com.br/Attraction_Review-g303322-d318128-Reviews-Congresso_Nacional-Brasilia_Federal_District.html", headers=headers)
avaliacao = re.findall(r'<span class="biGQs _P pZUbB SZRPS KxBGd">([\w.]+) avaliações</span>', website.text)
nota = re.findall(r'<div class="biGQs _P fiohW therk uuBRH">([\w.]+)</div>', website.text)

#agora é só printar usando o numero 0

print('Resultado da coleta de dados:')
print(f'Nota: {nota[0]}, Avaliação: {avaliacao[0]}')
