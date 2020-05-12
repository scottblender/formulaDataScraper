
import urllib.request #, urllib.error, urllib.parse
import re

#connect to a URL
dataURL = 'https://www.sae.org/attend/student-events/formula-sae-lincoln/awards-results'
baseURL = 'https://www.sae.org'
website = urllib.request.urlopen(dataURL)

#read html code
html = website.read().decode('utf-8')


beginningPattern = 'href="'
endPattern = '">Results'

#use re.findall to get all the links

results = re.findall( beginningPattern + '.*?' + endPattern, html)



for result in results:
    if '_ev_' not in result:    # removes results from electric vehicle (ev) competitions 
        url = baseURL + result[len(beginningPattern):-len(endPattern)]
        name = url[url.rfind('/')+1:]
        urllib.request.urlretrieve(url , name)
