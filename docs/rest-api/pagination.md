The majority of requests for multiple objects have parameters to manage pagination.  By returning results in separate pages, we can minimise 
network traffic and reduce the load on the server.  The size or limit (`max`) and starting position (`offset`) of each page can be passed in as a 
parameter 
to the query.  The response will always return the total number of objects, along with a list of 'items' corresponding to the specified 'page' of 
results.

##Response format 

For example, consider the endpoint that lists all folders in the system:

!!! abstract "API Endpoint"
    ```http
    POST /api/folders
    ```
The response body would look something like:

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "count": n,
        "items": [
            {
                ...
            },
            ...
        ]
    }
    ```
where `n` is the total number of folders available.  


## Parameter format

To manually specify the `offset` and `max` values, these should be passed as form paramters - for example the request:

!!! abstract "API Endpoint"
    ```http
    POST /api/folders?offset=10&max=5
    ```

would return folders 10-14 inclusive in the overall list.

To specify that all results should be returned, the boolean parameter `all` can be passed - for example the request:

!!! abstract "API Endpoint"
    ```http
    POST /api/folders?all=true
    ```

will return the complete list of visible folders.

The `all` parameter is an alternative, and should not be specified at the same time as `offset` and `max`.

## Default settings 

If no parameters are passed, the default values are:

-  `offset` : 0
- `max`: 10