import requests
import json

while(1):
    myFile = open("typereq.csv", "r+")
    if myFile.readline(1) == '$':
        
        req = myFile.readline()
        ret = requests.get('https://pokeapi.co/api/v2/pokemon/' + req).text
        if ret != "Not Found":
            retdict = json.loads(ret)

            myFile.seek(0)
            myFile.write((retdict['types'][0]['type']['name']).capitalize())
            if (len(retdict['types']) == 2):
                myFile.write("," + (retdict['types'][1]['type']['name']).capitalize())
            myFile.truncate()    
        else:
            myFile.seek(0)
            myFile.write("Pokemon Not Found")
    myFile.close()