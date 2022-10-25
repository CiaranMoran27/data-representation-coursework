import requests
from github import Github
from config import github_key as cfg                                # import token dict 

token = cfg["key"]                                                  # access token value
g = Github(token)                                                     # store access token     
repo = g.get_repo("CiaranMoran27/aprivateone")                      # get target repo     

file_info = repo.get_contents("assignment04_string_replace.txt")    # get contents of target file in repo 
file_url = file_info.download_url                                   # get url of target file   

response = requests.get(file_url)                                   # make http request to file url and 
file_content = response.text                                        # output the contents of the file
new_file_content = file_content.replace("Andrew", "Ciaran" )        # replace all instances of lecturer's name with my name

# Update the contents of the file on git up by using library function
# pass the path, commit message, the new file content and file sha (the sha is unique ID for your commit)
github_resp = repo.update_file(file_info.path,"Replaces substrings Andrew with Ciaran", new_file_content, file_info.sha)
print(github_resp)