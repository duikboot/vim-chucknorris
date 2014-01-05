# import vim
import json
import urllib
import html2text

link = "http://api.icndb.com/jokes/random"


def shuffle():
    try:
        js = urllib.urlopen(link).read()
    except:
        print "Website is not reachable."
        return
    d = json.loads(js)
    joke = d['value']['joke']
    joke = html2text.html2text(joke).strip().replace("\n", ' ')
    print joke
    return
