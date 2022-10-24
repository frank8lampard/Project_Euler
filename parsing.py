import urllib.request

opener = urllib.request.FancyURLopener({})
url = input("Введите url: ") 
f = opener.open(url)
content = f.read()