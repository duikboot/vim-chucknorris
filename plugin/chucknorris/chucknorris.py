# import vim
import json
import urllib2
import html2text

random_link = "http://api.icndb.com/jokes/random"


def shuffle():
    try:
        js = urllib2.urlopen(random_link, '', 3).read()
    except urllib2.URLError:
        print "Connection timed out"
        return
    except:
        print "Error occurred"
        return
    json_string = json.loads(js)
    joke = json_string['value']['joke']
    joke = html2text.html2text(joke).strip().replace("\n", ' ')
    print joke
    return

if __name__ == "__main__":
    shuffle()
