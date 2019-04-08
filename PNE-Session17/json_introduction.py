'''

JSON FORMAT (https://realpython.com/python-json/)

When exchanging data between a browser and a server, the data can only be text.

JSON is text, and we can convert any JavaScript object into JSON, and send JSON to the server.

We can also convert any JSON received from the server into JavaScript objects.

But, we are using python. SURPRISE! We can also use it with this language.

The JSON format is a standard for managing data very easily. It allow us to define the structure of our data.

Some of the differences between python language and json language:

Python	                JSON
dict                    object
list,tuple              array
str	                    string
int, long, float	    number
True	                true
False	                false
None	                null

Some vocabulary:

The process of encoding JSON is usually called serialization. This term refers to the transformation of data into a
series of bytes (hence serial) to be stored or transmitted across a network. You may also hear the term marshaling, but
that’s a whole other discussion. Naturally, deserialization is the reciprocal process of decoding data that has been
stored or delivered in the JSON standard.

That sounds pretty technical. Definitely. But in reality, all we’re talking about here is reading and writing. Think of
it like this: encoding is for writing data to disk, while decoding is for reading data into memory.


SERIALIZING JASON


'''

