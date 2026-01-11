# Basics of HTTP/HTTPS

## 1. Differences between HTTP and HTTPS
- **Security:** HTTP sends data in plain text, making it vulnerable to eavesdropping. HTTPS uses SSL/TLS encryption to protect data.
- **Port:** HTTP typically uses port 80, while HTTPS uses port 443.
- **Trust:** HTTPS requires a Digital Certificate to verify the identity of the web server.

## 2. HTTP Request/Response Structure
- **Request:** Includes a Request Line (Method, Path, Version), Headers (Metadata), and an optional Body (Data).
- **Response:** Includes a Status Line (Version, Status Code, Message), Headers, and a Body (Content).

## 3. Common HTTP Methods
- **GET:** Retrieves data from a server (e.g., fetching a web page).
- **POST:** Submits new data to be processed (e.g., submitting a form).
- **PUT:** Updates an existing resource entirely.
- **DELETE:** Removes a specific resource.

## 4. Common Status Codes
- **200 OK:** The request was successful.
- **201 Created:** A new resource was successfully created.
- **400 Bad Request:** The server cannot process the request due to client error.
- **404 Not Found:** The requested resource could not be found.
- **500 Internal Server Error:** The server encountered an unexpected condition.
