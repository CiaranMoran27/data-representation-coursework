import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

page = requests.get(url)
doc = parseString(page.content)

# check it works
'''print (doc.toprettyxml())''' #output to console comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later
'''with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)'''

# Modify the program to print out each of the trainscodes. I.e. find the listings and
# iterate through them to print each traincode out. Check it works
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")                  # get list of objects node positions
for objTrainPositionsNode in objTrainPositionsNodes:                                    # iterate them    
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)         # for each iteration get declared childnode positions
    traincode = traincodenode.firstChild.nodeValue.strip()                                  # access childnode value



dataList = []
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList.append(traincode)
    train_writer.writerow(dataList)


dataListAll = []
retrieveTags = ['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

with open('week03_train_all.csv', mode='w', newline='') as train_file_all:
    train_writer_all = csv.writer(train_file_all, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")                 
    for objTrainPositionsNode in objTrainPositionsNodes:                                    
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)               
            print(datanode.firstChild.nodeValue.strip())
            dataListAll.append(datanode.firstChild.nodeValue.strip())
    train_writer_all.writerow(dataListAll)