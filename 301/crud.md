# Crud - The Programming Kind

CRUD stands for Create, Read, Update and Delete which is used when describing computer storage.

## Status Codes

The following are a few status codes meanings:

- Status code 100’s mean that everything so far is alright and that the computer will continue its request to the server.
- Status code 200’s mean that a web request was completely accepted by the server successfully. It does not necessarily mean that the response was sent successfully.
- Status code 300’s mean that the resource or the server site being referenced is no longer available.
- Status code 400’s are essentially user error. They usually mean that improper information for the request was sent out.
- Status code 500’s mean that there is an issue with the server, essentially a try again later error.

1. A status code 200 is the basic code to let the user know that the information was sent successfully to the server.
2. A status code 308 means that the server site being accessed has moved to a different URL.
3. A code 204 is used if an update did not return data to a client.
4. A 410 Gone code is used if a resource used to exist but no longer does.
5. The Forbidden status code is used if the authorization passes but still cannot access the resource.

## Rest APIs a Few Ways

1. We need to pull our MongoDB database string out of our server and put it into our .env because this allows it to be accessed from the server.
2. Middleware is software that can link an operating system with the applications tunning on it.
3. The app.use(express.json()) is for recognizing an incoming object as a Json object from the middleware.
4. In a route, the /:id means a search for a directory.
5. Put and Patch both replace a bit of data. They are different because Put will replace the entire bit of data whereas Patch will replace a portion of the data.
6. You make a value in a schema by setting the default schema in the model.
7. A 500 error code status means server error.
8. The difference between a status 200 and a status 201 is that a 200 error means that an object was created and returned but a 201 error means that an object was created but only its reference was returned.


[Reading Notes Home Page](README.md)