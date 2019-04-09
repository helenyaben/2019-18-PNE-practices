"""

Study this API: http://www.icndb.com/api/ and write a python program that should do the following, each time
you execute it:

(1) Print on the console the following information:
  -The number of total jokes about Chuck Norris available at the database.
  -The number and names of the different categories.
  -A random joke :-)

"""
import termcolor
import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
chuck_jokes = json.loads(text_json)

jokes = chuck_jokes["value"]

#Create two empty list, one for id and another for categories
id_list = []
cat_list =[]


for element in range(len(jokes)):

    id = jokes[element]["id"]
    id_list.append(id)

    cat = jokes[element]["categories"]

    for i in range(len(cat)):
        cat_list.append(cat[i])

# Transform the list of categories which has each category of each joke into a list with the named of different categories

cat_list =list(dict.fromkeys(cat_list))


print("The number of jokes is: {}".format(max(id_list)))

print('Different categories: '.format(len(cat_list)))
for element in cat_list:
    print(' -', element.capitalize())

