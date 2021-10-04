# APIs

1. REST stands for Representational State Transfer.
2. According to the Microsoft Documents [here](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design) "REST APIs are designed around *resources*, which are any kind of object, data, or service that can be accessed by the client"
3. An identifier of a resource is A URI (Uniform Resource Identifier) that uniquely identifies the resource. An example is a link to an order page with one particular order's information.
4. The most common HTTP verbs are GET, POST, PUT, PATCH and DELETE.
5. The URIs should be based on nouns ie. the resource and not verbs ie. the operation of the resource.
6. An example of a good URI is http://websitestore.com/orders
7. A 'chatty' web API is one that makes several small requests to the server. It is a bad thing. It is much better to request larger packets of data at a time.
8. The status code of a successful GET request will return 200.
9. The status code of an unsuccessful GET request will return 404.
10. The status code of a successful POST request will return 201 or 200.
11. The status code of a successful DELETE request will return 204.

My name using RegEx would be written as << J >><< a >><< e >>,

[Reading Notes Home Page](README.md)