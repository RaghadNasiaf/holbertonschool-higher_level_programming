# 0. Basics of HTTP/HTTPS

## Differentiating HTTP and HTTPS
* **HTTP (Hypertext Transfer Protocol):** The foundational protocol for data communication on the web. It transfers data in plain text, meaning that anyone eavesdropping on the communication can see the content, making it insecure.
* **HTTPS (HTTP Secure):** An extension of HTTP that adds a layer of encryption using SSL/TLS. This makes the content unintelligible to eavesdroppers, providing security for sensitive data like banking or email.

## HTTP Request and Response Structure
Communication involves a client sending a request and a server returning a response.

### Request Structure:
* **Method:** Specifies the action (e.g., GET, POST).
* **Path:** The location of the resource on the server.
* **Headers:** Metadata about the request (e.g., User-Agent).
* **Body:** Optional data sent with the request.

### Response Structure:
* **Status Code:** Indicates the result of the request (e.g., 200 OK).
* **Headers:** Metadata about the server and response.
* **Body:** The actual data or resource returned.

## Common HTTP Methods
* **GET:** Retrieves data from a server. *Use case: Fetching a web page or data from an API*.
* **POST:** Submits new data to be processed by the server. *Use case: Creating a new resource or submitting a form*.
* **PUT:** Updates an existing resource on the server. *Use case: Modifying an existing record*.
* **DELETE:** Removes a specific resource. *Use case: Deleting a file or database entry*.

## Common HTTP Status Codes
* **200 OK:** The request succeeded. *Scenario: A webpage loads successfully*.
* **201 Created:** A resource was successfully created. *Scenario: A new user account is registered*.
* **400 Bad Request:** The server cannot process the request due to client error. *Scenario: Invalid syntax in the request*.
* **404 Not Found:** The requested resource is not available on the server. *Scenario: Accessing a page that does not exist*.
* **500 Internal Server Error:** The server encountered an unexpected error. *Scenario: A server-side script or database failure*.
