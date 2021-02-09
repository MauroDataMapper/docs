---
title: REST API Introduction
summary: This page explains the purpose and architecture of the Metadata Catalogue REST API.
authors:
    - James Welch
date: 19th Aug 2019
---

The Metadata Catalogue API conforms to standard [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles.  The API has 
resource-oriented URLs, accepts XML and JSON body content (or form-encoded parameters where applicable), and can return data in XML or JSON 
formats. Each call uses standard HTTP response codes, authentication, and verbs.

## Requests

To make a REST API request, you combine:

* The HTTP method: `GET`, `POST`, `PUT`, `PATCH` or `DELETE`
* The URL to the API service - for example `http://modelcatalogue.cs.ox.ac.uk/demo/api`
* The URI to a resource to query, update or delete
* One or more [HTTP request headers](#http-request-headers), for example the identifier of any session token, or a request to save data back in XML
 or 
JSON format.

Most calls may also require a JSON or XML body representing any new or updated data, or query parameters to filter or restrict the response. 

## HTTP request headers

The commonly-used HTTP request headers used are:

### Accept

This header determines the format of the response body for those requests with structured output.  The syntax is:

```http
Accept: application/<format>
```

where `<format>` can be either `xml` or `json`.

By default, the format of the response body will match that of the request body, where applicable.  

### Content-Type

This header specifies the format of the request body, where applicable.  The syntax is:

```http
Content-Type: application/<format>
```

where `<format>` can be either `xml` or `json`.

By default, the request body is assumed to be JSON unless otherwise specified

### Cookie

This header stores the [session identifier](https://javarevisited.blogspot.com/2012/08/what-is-jsessionid-in-j2ee-web.html) which persists a login between calls.  For example, having received a session cookie during 
[login](authentication.md#login), the token can be used to validate the user.  

```http
Cookie: JSESSIONID=<sessionid>
```

Typically, a session identifier is 32 characters long and uses hexadecimal characters `0-9`, `A-F`


## Tools

We use [Postman](../postman) for testing API calls during development.  It has an intuitive interface that lets you set 
parameters, headers, and message bodies, and preview structured responses.  It can also be used as part of an automated testing or debugging requests.

If you're looking for a more lightweight solution, [curl](https://curl.haxx.se/docs/manpage.html) is a suitable command-line tool which can be 
easily configured to make complex REST API requests.  In this set of documentation, requests are illustrated with the appropriate curl command.

## Testing

There is a test api resource which will show whether the server api is running correctly, and whether the client has been correctly configured.  

To test this using `curl`, run the following command:

```bash
curl -X GET http://localhost:8080/api/test 
```

This will return the following JSON:

=== "Response body (JSON)"
    ```json
    {
       "message":"Not Found",
       "error":404,
       "path":null,
       "object":null,
       "id":null
    }
    ```





