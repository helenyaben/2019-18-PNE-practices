'''

ACCESSING REMOTE DATA : API REST

For accessing to remote data, first we need to know what servers are available, and what is the web interface they
provide.


For accessing to the services/data provided by the server, we should read its API documentation carefully. Every server defines its own names and parameters. It is important to understand the terminology:

(1) Hostname: We need to know the hostname of the server we want to access. This name should NOT include http:// or a slash in the end. This is an example of a correct hostname: aws.random.cat

(2) HTTP method: We should know the method used for the request: GET or POST

(3) Headers: Some services require the client to send information on the request heathers

(4) The endpoints: This is the name given to the resources provided by the server. For example: "/meow", or "/users".
Simply put, an endpoint is one end of a communication channel. When an API interacts with another system, the touchpoints
of this communication are considered endpoints. For APIs, an endpoint can include a URL of a server or service.
Each endpoint is the location from which APIs can access the resources they need to carry out their function.

APIs work using ‘requests’ and ‘responses.’ When an API requests information from a web application or web server, it will receive a response. The place that APIs send requests and where the resource lives, is called an endpoint.

(5) The parameters: Some endpoints require parameters. Some parameters are optional, others mandatory. Parameters can
be given in two places:

  - As part of the endpoint name: For example, for accessing to the user repos in github, the endpoint is like this:
  /users/:user/repo. In this example, :user is the parameter and should be changed for the real username
  - As an external parameter: This parameters are located after the ? symbol, in the end of the endpoint. The syntax is: "parameter=value". Different parameters are separated by the & or + symbols. For example: /sequence/id/ENSG00000157764?content-type=application/json

(6) The data FORMAT: We should know in which format the DATA is returned: JSON, XML, other...

'''