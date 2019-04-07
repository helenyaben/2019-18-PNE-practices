'''

HTTP MODULE

Python includes an HTTP module for implementing both HTTP clients and servers very easily.
we will learn how to program servers using the HTTP module.

After downloading the html documents, write this in the terminal:

python3 -m http.server 8000

Now go to the browser and write one of the following:
- http://localhost:8000
- http://0.0.0.0:8000/
- http://your-ip:8000/

WEB SERVERS : HTTTP SERVERS MODULE

Now we are going to create our first Web Server.

Information from: https://www.afternerd.com/blog/python-http-server/

An HTTP web server is nothing but a process that is running on your machine and does exactly two things:

1- Listens for incoming http requests on a specific TCP socket address (IP address and a port number which I will talk about later)

2- Handles this request and sends a response back to the user.

When you type www.yahoo.com on your browser, your browser will create a network message called an HTTP request.

This Request will travel all the way to a Yahoo computer that has a web server running on it. This web server will intercept
your request, and handle it by responding back with the html of the Yahoo home page. Finally your browser renders this
html on the screen and that’s what you see on your screen.

Every interaction with the Yahoo home page after that (for example, when you click on a link) initiates a new request
and response exactly like the first one.
To reiterate, the machine that receives the http request has a software process called a web server running on it.
This web server is responsible for intercepting these requests and handling them appropriately.

But, how does the request reach that yahoo machine in the first place?

Any http message (whether it is a request or response) needs to know how to reach its destination.
In order to reach its destination, each http message carries an address called the destination TCP address.
And each TCP address is composed of an IP address and a port number.

So where is that address when all you did was type www.yahoo.com on your browser?

Well, this domain name is converted into an IP address through a large distributed database called the DNS.

The IP address alone will allow the HTTP message to arrive at the right machine, but you still need the port number in
order for the HTTP request to arrive exactly at the web server.
In other words, the web server is a regular network application that is listening on a specific port. And the http request MUST be addressed to that port.

So where is the port number when you type www.yahoo.com?

By default, the port number is 80 for http and 443 for https, so even though you haven’t explicitly specified the port number, it is still there.

In order to create a web server in Python 3, you will need to import two modules: http.server and socketserver.

'''

