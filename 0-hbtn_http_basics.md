# Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS
- HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content.
- HTTPS adds a layer of encryption using SSL/TLS, making the content unintelligible to eavesdroppers.
- The "s" in "https" stands for "secure".

## 2. Understanding HTTP Structure
- **Request:** Includes a Method (GET, POST), Path, Version, Headers, and an optional Body.
- **Response:** Includes a Status Line (Version, Status Code like 200 OK), Headers, and a Body.

## 3. Common HTTP Methods
- **GET:** Retrieves data; Use case: Fetching a web page or data from an API.
- **POST:** Submits new data to be processed.
- **PUT:** Updates an existing resource.
- **DELETE:** Removes a specific resource.

## 4. Common Status Codes
Status codes are grouped by their first digit:
- **1xx:** Informational.
- **2xx:** Successful (e.g., 200 OK).
- **3xx:** Redirection.
- **4xx:** Client errors (e.g., 404 Not Found: When a requested resource isn't available).
- **5xx:** Server errors (e.g., 500 Internal Server Error).
