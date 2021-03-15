The majority of requests for multiple objects have parameters to manage pagination.  By returning results in separate pages, we can minimise 
network traffic and reduce the load on the server.  The size or limit (`max`) and starting position (`offset`) of each page can be passed in as a 
parameter 
to the query.  The response will always return the total number of objects, along with a list of 'items' corresponding to the specified 'page' of 
results.

---

## Parameter format

In these examples we consider the endpoint endpoint for listing all folders:

<endpoint class="get">/api/folders</endpoint>

To manually specify the `offset` and `max` values, these should be passed as form parameters - for example the request:
    
<endpoint class="get">/api/folders?offset=10&max=5</endpoint>

Would return folders 10-14 inclusive in the overall list.

To specify that all results should be returned, the boolean parameter `all` can be passed - for example the request:

<endpoint class="get">/api/folders?all=true</endpoint>

Will return the complete list of visible folders.

The `all` parameter is an alternative, and should not be specified at the same time as `offset` and `max`.

---

## Response format 

Again consider the endpoint endpoint for listing all folders described above.

The response body would look something like:

=== "Response body (JSON)"
    ```json
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
Where `n` is the total number of folders available.  The number of `items` returned will be at most `max` items.

---

## Default settings 

If no parameters are passed, the default values are:

-  `offset` : 0
- `max`: 10

---