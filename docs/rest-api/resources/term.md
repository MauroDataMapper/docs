A Term is part a [Terminology](terminology.md) and can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "Term",
        "model": "20b1fd65-a7bf-4a39-a14b-c80b0174b03e",
        "code": "CT1",
        "definition": "Custom Term",
        "label": "CT1: Custom Term",
        "lastUpdated": "2021-04-28T10:10:13.945Z"        
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this term
- **domainType** (Type): The domain type of this catalogue object. Will always be `Term` in this case.
- **model** (UUID): The unique identifier of the owning data model
- **code** (String): A unique code identifier for the term.
- **definition** (String): The definition/name of this term.
- **label** (String): The human-readable identifier of this term. This is the combination of `code` and `definition`.
- **lastUpdated** (DateTime): The date/time when this term was last modified

As well as the endpoints listed below, a term is also a CatalogueItem, and so a term identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Getting information

The following endpoint returns a [paginated](../pagination.md) list of all the terms within a particular Terminology.

<endpoint class="get">/api/terminologies/**{terminologyId}**/terms</endpoint>

This endpoint provides the detailed information about a particular term.

<endpoint class="get">/api/terminologies/**{terminologyId}**/terms/**{id}**</endpoint>

## Create / Update / Delete

To create a new term from scratch, use the following _post_ endpoint with a JSON request body similar to above.

<endpoint class="post">/api/terminologies/**{terminologyId}**/terms</endpoint>

To edit the properties of a term, use the following endpoint, with a body similar to the JSON described at the top of this page.

<endpoint class="put">/api/terminologies/**{terminologyId}**/terms/**{id}**</endpoint>

To delete a term, use the following endpoint.

<endpoint class="delete">/api/terminologies/**{terminologyId}**/terms/**{id}**</endpoint>

## Relationships

<endpoint class="get">/api/terminologies/**{terminologyId}**/terms/**{termId}**/termRelationships</endpoint>
<endpoint class="get">/api/terminologies/**{terminologyId}**/terms/**{termId}**/termRelationships/**{id}**</endpoint>
<endpoint class="post">/api/terminologies/**{terminologyId}**/terms/**{termId}**/termRelationships</endpoint>
<endpoint class="put">/api/terminologies/**{terminologyId}**/terms/**{termId}**/termRelationships/**{id}**</endpoint>
<endpoint class="delete">/api/terminologies/**{terminologyId}**/terms/**{termId}**/termRelationships/**{id}**</endpoint>
