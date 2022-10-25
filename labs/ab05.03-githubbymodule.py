






from github import Github
from config import apiGithubKey as cfg


apikey = cfg["apiKey"]

g = Github(apikey)
#for repo in g.get_user().get_repos():
    #print(repo.name)


'''
Modify the program to get the clone url of a repository on your account m(you could make
a private one just for this if you wish). Put a file in the repository called test.txt
'''

repo = g.get_repo("CiaranMoran27/dataRepTestTxt")
#print(repo.clone_url)

'''
Get the downloadurl of the file in this repository called test.txt (make sure that there is a file
called test.txt in there
'''

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

'''
Use the download URL to make a http request to the file can output the contents of the file
(TEXT contents).
'''
import requests
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

'''
 Append the text more stuff (with a newline character) to the contents of the file
'''
#newContents = contentOfFile + " more stuff ...\n"
#print(newContents)


'''
Update the contents of the file on git up by using the function
''' # what is fileinfo.sha???

#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog", newContents, fileInfo.sha)
#print (gitHubResponse)