import webbrowser

import requests

pageurl = "http://github.com"
date1 = 2012810
date2 = 2017810
date3 = 2008810

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
