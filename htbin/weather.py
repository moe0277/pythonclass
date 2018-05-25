'''
Created on May 17, 2018

@author: mkhan
'''
import urllib.request
import json

APIKEY="5019fd36b732b177c791a9e4a4bd4742"

class Weather(object):
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=%s" % (self.zipcode, APIKEY) 
        self.proxies = {'http': 'http://www-proxy:80/'}
        self.opener = urllib.request.FancyURLopener(self.proxies)
         
    def getWeather(self):
        try: 
            req = self.opener.open(self.url)
            reqstr = req.read()
        except:
            req = urllib.request.urlopen(self.url)
            reqstr = req.read()
        result = json.loads(reqstr)
        return result
        
    
if __name__ == "__main__":
    w = Weather(78741)
    data = w.getWeather()   
    print(data)
    print(data['coord'])
    