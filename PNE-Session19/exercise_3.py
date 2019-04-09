'''

Exercise 3: information about a github user

Create a python program that ask the user for a github username and print on the console the following information about
that username:

-Real name
-The list with the names of all the repos the user has
-The total number of commits to the 2018-19-PNE-repo

'''


import http.client
import json

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "Obijuan"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))

"""
REQUEST 2: 
-NAMES OF THE PUBLIC REPOS
-TOTAL NUMBER OF COMMITS IN THE 2019-18-PNE-practices repo
 """


import http.client
import json

HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "Obijuan"
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

user = json.loads(text_json)

login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: \n{}".format(bio))



