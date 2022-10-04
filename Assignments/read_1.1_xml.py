from xml.dom.minidom import parse
import os

dirname = os.path.dirname(__file__)                                             # get folder directory file is in
filename = os.path.join(dirname, 'Assignment_1.1.xml')                          # join filename to folder directory

retrieveTags = ['ISBN', 'Title', 'Author']

with open(filename, mode='r') as f:
    dom =  parse(f)
    objPositionNode = dom.getElementsByTagName("Book")                              # get book element object positions into list
    for objPositionsNode in objPositionNode:                                        # iterate book object position nodes
        for retrieveTag in retrieveTags:                                                
            datanode = objPositionsNode.getElementsByTagName(retrieveTag).item(0)           # iterate child object position nodes via retrieveTags list               
            print(datanode.firstChild.nodeValue.strip())                                    # print child node value