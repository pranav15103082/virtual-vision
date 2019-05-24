from Commander.commander import commander
import urllib2
from validcommands import commands as co

#body of mainloop
def mainloop():
    if internet_on():
        #activate system commandset
        commander.main()
    else:
        raise Exception('check internet connection and try again')


#function for checking net connectivity
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

#starting mainloop
mainloop()
