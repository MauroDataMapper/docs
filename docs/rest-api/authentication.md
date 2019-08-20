The Metadata Catalogue stores content that may be either publicly accessible, or have access restricted to particular users or groups.  Therefore 
the majority of API requests can be made as an anonymous user (by passing no session information in the request header), or as a logged in user (by
passing a valid session key in the request headers.)
 
A request to the `login` will result in a new session token being generated.  This is typically 32 hexadecimal characters in length, and uniquely 
identifies the current session.  These tokens should not be shared, and will automatically expire with 30mins of inactivity.  Sessions can be 
manually terminated through a call to the `logout` resource.   At any point the validity of a session may be checked against the server.

##Login

To login to the server 

| Endpoint |
| -------- |
| `GET /api/login` |


##Session validation

##Logout