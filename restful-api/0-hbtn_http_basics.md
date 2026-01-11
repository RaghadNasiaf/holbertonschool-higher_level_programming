# Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS
- HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content.
- HTTPS adds a layer of encryption using SSL/TLS, making the content unintelligible to eavesdroppers.
- The "s" in "https" stands for "secure".

## 2. Understanding HTTP Structure
- **Request:** Includes a Method (e.g., GET, POST), Path, HTTP Version (e.g., HTTP/1.1), Headers, and an optional Body.
- **Response:** Includes a Status Line (Version, Status Code like 200 OK), Headers, and a Body.

## 3. Common HTTP Methods
- **Method:** GET, Description: Retrieves data, Use case: Fetching a web page or data from an API.
- **Method:** POST, Description: Submits new data to be processed, Use case: Submitting a form or creating a resource.
- **Method:** PUT, Description: Updates an existing resource, Use case: Updating user profile information.
- **Method:** DELETE, Description: Removes a specific resource, Use case: Deleting a user account or post.

## 4. Common Status Codes
- **Status Code:** 200, Description: OK, Scenario: When a request is successful and the server returns the requested data.
- **Status Code:** 301, Description: Moved Permanently, Scenario: When a resource has been permanently moved to a new URL.
- **Status Code:** 404, Description: Not Found, Scenario: When a requested page or resource isn't available on the server.
- **Status Code:** 500, Description: Internal Server Error, Scenario: When the server encounters an unexpected condition.

Status codes are grouped by their first digit:
- **1xx:** Informational.
- **2xx:** Successful.
- **3xx:** Redirection.
- **4xx:** Client errors.
- **5xx:** Server errors.
