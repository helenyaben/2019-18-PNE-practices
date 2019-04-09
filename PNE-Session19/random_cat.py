'''

We all know that the fast development of Internet was due to the cats. It is a fact! :-) If we have a look at the public
APIs we will find some of them related to cats. Let's chose this one: RandomCat. This is a services that returns the URL
of a random cat image. So, everytime we invoke the service, we will receive a different URL (that correspond to a
different image).

The service provided by the RandomCat server is so simple, that there is not have any documentation. So, let's try to
figure out the information by ourselves. Before programming anything, it is important to test the API with the Browser,
to check if we understand it correctly. Then we can proceed to program the client

Let's open this URL in the browser: https://aws.random.cat/meow (with mozzilla firefox)

We analyze it and write down all the required information for accessing to it:

(1) Protocol: HTTPS, we can see it in the URL.
(2) Host name: aws.random.cat
(3) HTTP method: GET. This is what the header Access-Control-Allow-Methods say.
(4) DATA FORMAT: JSON. We have checked in on the Content-Type header: application/json.
(5) Endpoint: /meow
(6) Parameters: none

Analyzing the JSON file, we see that it represents an object, which has the file property. The value of this property
is the URL where the image is located.

Now that we have collected all the information, we can proceed to program the client. It will connect to the server, get
the URL and print it on the console.

'''
