# Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS
- **HTTP:** Does not encrypt data; anyone eavesdropping can see the content in plain text.
- **HTTPS:** Adds a layer of security using SSL/TLS encryption, making content unintelligible to eavesdroppers.
- **The "s":** In HTTPS, the "s" stands for "secure".

## 2. Understanding HTTP Structure
- **Request:** Includes Method (e.g., GET), Path, Protocol Version, Headers (e.g., Host, User-Agent), and an optional Body.
- **Response:** Includes a Status Line (Version, Status Code 200 OK), Headers (e.g., Content-Type), and a Body (e.g., HTML/JSON content).

## 3. Common HTTP Methods
- **GET:** Retrieves data from a server; used for fetching a web page or data from an API.
- **POST:** Submits new data to the server to create resources.
- **PUT:** Updates an existing resource on the server.
- **DELETE:** Removes a specific resource from the server.

## 4. Common HTTP Status Codes
Status codes are grouped by their first digit:
- **1xx:** Informational.
- **2xx:** Successful (e.g., **200 OK** means the request succeeded).
- **3xx:** Redirection (e.g., **301 Moved Permanently**).
- **4xx:** Client Errors (e.g., **404 Not Found** when a resource is unavailable).
- **5xx:** Server Errors (e.g., **500 Internal Server Error**).
