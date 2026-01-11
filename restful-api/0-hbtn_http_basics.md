# Basics of HTTP/HTTPS

## 1. Differences between HTTP and HTTPS
- **Security:** HTTP sends data in plain text, making it vulnerable to interception. HTTPS encrypts data using SSL/TLS, making it secure.
- **Port:** HTTP typically uses port 80, while HTTPS uses port 443.
- **Trust:** HTTPS requires a Digital Certificate to verify the identity of the server.

## 2. HTTP Request/Response Structure
- **Request:** Includes a Request Line (Method, Path, Version), Headers (Metadata), and an optional Body (Data).
- **Response:** Includes a Status Line (Version, Status Code, Message), Headers, and a Body (Content).

## 3. Common HTTP Methods
- **GET:** Retrieves data from a server.
- **POST:** Submits new data to be processed.
- **PUT:** Updates an existing resource entirely.
- **DELETE:** Removes a specific resource.

## 4. Common Status Codes
- **200 OK:** Request succeeded.
- **201 Created:** New resource successfully created.
- **400 Bad Request:** Server cannot process the request due to client error.
- **404 Not Found:** Resource not found on the server.
- **500 Internal Server Error:** Unexpected server-side error.
