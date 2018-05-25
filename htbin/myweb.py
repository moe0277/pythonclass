'''
Created on May 17, 2018

@author: mkhan
'''
import cgi
import cgitb; cgitb.enable()
import weather
import pytemperature


header="Content-Type: text/html\n\n"
page1="""<!DOCTYPE html>
<html>

<head>
<title>Weather App</title>
</head>

<body>
<form name="weatherForm">
    <p>Zip Code: <input type="text" name="zipcode"></input>
    <br/>
    <input type="submit"></input>
</form>
<hr/>
Page Visits: %s
</body>
</html>"""


page2="""<html>
<head>
<title>Weather App</title>
</head>

<body>
<p>For Zip Code: %s </p>
<br />
<p>Weather data: </p>
</body>
<html>"""


print(header)

def pageVisit():
    fin = open("count.txt", "r")
    count = fin.read()
    count = int(count)
    count += 1
    fin.close()
    
    fout = open("count.txt", "w")
    fout.write(str(count))
    fout.close()
    return count



form = cgi.FieldStorage()
if "zipcode" not in form:
    #count = pageVisit()
    count = 0
    print(page1 % count)

else:
    zip = form['zipcode'].value
    myw = weather.Weather(zip)
    res = myw.getWeather()
    print(page2 % zip)
    print("<pre>%s</pre>" % res)
    kelvin = res['main']['temp']
    myf = pytemperature.k2f(kelvin)
    print("<pre>My Temperature: %sF</pre>" % myf)