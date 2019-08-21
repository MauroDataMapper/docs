The Metadata Catalogue stores content that may be either publicly accessible, or have access restricted to particular users or groups.  Therefore 
the majority of API requests can be made as an anonymous user (by passing no session information in the request header), or as a logged in user (by
passing a valid session key in the request headers.)
 
A request to the `login` will result in a new session token being generated.  This is typically 32 hexadecimal characters in length, and uniquely 
identifies the current session.  These tokens should not be shared, and will automatically expire with 30mins of inactivity.  Sessions can be 
manually terminated through a call to the `logout` resource.   At any point the validity of a session may be checked against the server.

##Login

To login to the server, `POST` to the following API endpoint 

!!! abstract "API Endpoint"
    ```http
    POST /api/authentication/login
    ```

The request body should contain the username, and the password.  The username is not case-sensitive:

!!! abstract "Request body"
    ```json tab="JSON"
    { 
        "username" : "joe.bloggs@test.com",
        "password" : "pa55w0rd"
    }
    ```
    
    ```xml tab="XML"
    <user>
        <username>joe.bloggs@test.com</username>
        <password>pa55w0rd"</password>
    </user>
    ```

If successful, the response body will contain the user's `id`, email address, first and last names, their user role, and whether or not that 
user's account has been disabled (typically false in the case of a successful login)

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "id": "01234567-0123-0123-0123-01234567",
        "emailAddress": "joe.bloggs@test.com",
        "firstName": "Joe",
        "lastName": "Bloggs",
        "userRole": "EDITOR",
        "disabled": false
    }
    ```
    
One of the response headers will also contain an identifier for the new session.  The header is of the form:

```http
Set-Cookie: JSESSIONID=9257B45A4BCA750570736626C62EE74B; Path=/; HttpOnly
```      

The session id (JSESSIONID) can be passed to any subsequent request to ensure that the user's credentials are used.  To supply the cookie, it 
should be placed in the `Cookie` request header:

```http
Cookie: JSESSIONID=9257B45A4BCA750570736626C62EE74B
```

Further requests without the session cookie will be treated as anonymous requests.
    
##Session validation

In order to validate whether a session is currently active, or has expired (by logging out, or timed-out due to inactivity), 

!!! abstract "API Endpoint"
    ```http 
    GET /api/authentication/isValidSession
    ```

No request body or parameters are required for this request.  The response will be simply `true` or `false` depending on the validity of the 
session whose `JSESSIONID` is passed in as part of the request headers

!!! abstract "Response body"
    ```json tab="JSON"
    true
    ```

##Logout

Every session should ideally be closed manually, rather than leaving it to expire through inactivity.  In order to close a user session, you should
 call the logout endpoint, again including the `JSESSIONID` cookie as part of the request headers   

!!! abstract "API Endpoint"
    ```http 
    POST /api/authentication/logout
    ```

The response should include the status `200: OK`, and the successful response is simply the following text:

!!! abstract "Response body"
    ```text tab="Text"
    Successfully logged out
    ``` 