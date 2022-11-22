import json
from json2html import *

# Open the input file
with open('abc.json') as json_file:                 # or give path of the input file
    data = json.load(json_file)                     # this will load the json file into dat variable
    scanOutput = json2html.convert(json=data)       # it will convert Json to Html
    htmlReportFile = "output.html"                  # this will write the html file here/path
    with open(htmlReportFile, 'w') as htmlfile:     # open the html file
        htmlfile.write(str(scanOutput))             # write converted json into our created file
        print("json file converted successfully")
