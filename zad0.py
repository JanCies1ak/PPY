import webbrowser

import requests

pageurl = input("Podaj url")

date1 = input("Podaj date nr1 np: 20230228")
date2 = input("Podaj date nr2 np: 20230228")
date3 = input("Podaj date nr3 np: 20230228")

url1 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date1)
url2 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date2)
url3 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date3)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)

d = response1.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

d = response2.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

d = response3.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)
