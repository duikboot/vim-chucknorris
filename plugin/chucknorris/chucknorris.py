# import vim
import json
import urllib2
import html2text

link = "http://api.icndb.com/jokes/random"


def shuffle():
    try:
        js = urllib2.urlopen(link, '', 3).read()
    except urllib2.URLError:
        print "Connection timed out"
        return
    except:
        print "Error occurred"
        return
    d = json.loads(js)
    joke = d['value']['joke']
    joke = html2text.html2text(joke).strip().replace("\n", ' ')
    print joke
    return

if __name__ == "__main__":
    shuffle()
