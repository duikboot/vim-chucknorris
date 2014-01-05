# import vim
import json
import urllib
import html2text

link = "http://api.icndb.com/jokes/random"

def shuffle():
    js = urllib.urlopen(link).read()
    d = json.loads(js)
    joke = d['value']['joke']
    joke = html2text.html2text(joke).strip().replace("\n", ' ')
    print joke
