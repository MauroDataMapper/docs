The Metadata Catalogue API uses [standard HTTP response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) to indicate the success or 
the failure of an API request.  In addition, some requests also return additional status information relating to the reasons for any error or 
failure that has occurred.    

In general, codes of the form `2XX` indicate success, codes of the form `4XX` indicate an error with the request, and codes of the form `5XX` 
indicate that an error occurred with the server during the processing of a potentially valid request.Hopefully those in the last category are rare!
  More detail for each of the commonly-seen error codes is shown in the table below.
  
  
##Error code tables
 
| Code | Meaning | Description |
|------|---------|-------------| 
| **200**  | **OK**      | The response succeeded as expected            |
| **201**  | **Created** | The `POST` method was successful and a new resource was created |
| **204**  | **No Content** | The server successfully processed the request, but no content was returned - for example when deleting a resource |

| Code | Meaning | Description |
|------|---------|-------------| 
| **400**  | **Bad Request**  | The server cannot process the request - either a required parameter was missing, or the body was badly formatted |
| **401**  | **Unauthorized** | The requested resource requires [authentication](authentication.md), but none was provided as part of the header information  |
| **403**  | **Forbidden**  | The server refused to process the request because the authenticated user does not have the correct permissions  |
| **404**  | **Not Found** |  The resource requested could not be found.  This may be because the URL is malformed, or because the HTTP method was not permitted for this particular URL - for example `PUT` on a resource which may not be edited |
| **408**  | **Request Timeout** | The server gave up waiting for a request.  This code may occasionally be seen when the upload of a file takes longer than the server is prepared to wait. |
| **409**  | **Conflict** | The server could not process the request because of some conflict int he current state of the resource.  Most commonly this occurs when a user tried to log in, despite already benig logged in with a valid session. |

| Code | Meaning | Description |
|------|---------|-------------| 
| **500**  | **Internal Server Error** | This is a catch-all error message, when the request appears valid but the server was unable to process it.   This may well be caused by a bug in the software; such error messages may be reported through our issue-tracking software |
| **502**  | **Bad Gateway** | This is a system error relating to the server.  It may be that the Metadata Catalogue is configured incorrectly, or is otherwise not installed correctly. |
| **503**  | **Service Unavailable** | The API server is currently unavailable.  It may have been taken down for maintenance, or is otherwise not running |
| **504**  | **Gateway Timeout** | See `502` - the server may be badly configured or is otherwise unavailable |
