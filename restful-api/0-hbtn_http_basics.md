# Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS
- HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content.
- HTTPS adds a layer of encryption using SSL/TLS encryption, protecting data from eavesdroppers.
- The "s" in "https" stands for "secure".

## 2. Understanding HTTP Structure
- **Request:** Includes Method (e.g., GET, POST), Path, Headers, and an optional Body.
- **Response:** Includes a Status Line (Status Code like 200 OK), Headers, and a Body.

## 3. Common HTTP Methods
- **Method: GET**, Description: Retrieves data, Use case: Fetching a web page or data from an API.
- **POST:** Submits new data to be processed.
- **PUT:** Updates an existing resource.
- **DELETE:** Removes a specific resource.

## 4. Common Status Codes
- **1xx:** Informational.
- **2xx:** Successful (e.g., 200 OK).
- **3xx:** Redirection.
- **4xx:** Client errors (e.g., **Status Code: 404**, Description: Not Found, Scenario: When a requested page or resource isn't available on the server).
- **5xx:** Server errors.
