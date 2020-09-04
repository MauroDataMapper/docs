Classifiers are tags that can be used to organise or locate items in the catalogue, separately from the main folder tree.  
For example, if you've organised models in folders by organisation, then you may use classifiers to additionally organise 
them by disease type, or purpose.  Tags can be applied to any catalogue item 
(see [glossary / model](../../model/glossary.md)), and may be shared with other users / groups. 

As with other sharable resources in the catalogue, the API endpoints listed on this page may be called by 
authenticated or anonymous users; the results will differ depending on which classifiers, and which catalogue elements 
have been made available.  See the [endpoints for authentication](../authentication.md)

## Retrieving classifiers

To get a list of all existing classifiers visible to the current user, call 

<endpoint class="get">/api/classifiers</endpoint>

This will return a [paginated list](../pagination.md) in the form:

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "count": n,
        "items": [
            {
                "id": "123-456-abcd-efgh",
                "label": "Classifier label",
                "lastUpdated": "2019-01-01T00:00:00.000Z"
            },
            {
                ...
            },
            ...
        ]
    } 
    ```
To get more details about a particular classifier, call the same endpoint with the appropriate classifier id:

<endpoint class="get">/api/classifiers/**{id}**</endpoint>

This will return a single classifier, showing its top-level detail details, and whether the current user has 
editing writes to make changes:

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "id": "123-456-abcd-efgh",
        "label": "Classifier label",
        "lastUpdated": "2019-01-01T00:00:00.000Z",
        "editable": true
    } 
    ```

To get the list of catalogue items that have been tagged with a particular identifier, use the following endpoint:

<endpoint class="get">/api/classifiers/**{id}**/catalogueItems</endpoint>

This will return a [paginated list](../pagination.md) of catalogue items (data models, data classes, data elements, etc):

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "count": n,
        "items": [
            {
                "id": "123-456-abcd-efgh",
                "domainType": "DataModel",
                "label": "Data Model Name",
                "documentationVersion": "1.0.0",
                "description": "Data Mode Description",
                "semanticLinks": [ ... ]
            }
        ]
    }
    ```
    
Equivalently, to retrieve the list of classifiers associated with a given catalogue item, use the endpoint:

<endpoint class="get">/api/features/**{featureComponentId}**/classifiers</endpoint>

This will return a [paginated list](../pagination.md) of associated classifiers:

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "count": n,
        "items": [
            {
                "id": "123-456-abcd-efgh",
                "label": "Classifier label",
                "lastUpdated": "2019-01-01T00:00:00.000Z"
            },
            {
                ...
            },
            ...
        ]
    } 
    ```

## Creating classifiers

New classifiers can be created with a call to the `POST` endpoint:

<endpoint class="post">/api/classifiers</endpoint>

The request body must include the new classifier's label (which must be unique across the system):

!!! abstract "Request body"
    ```json tab="JSON"
        {
            "label":"My new classifier"
        } 
    ```

The response will include the identifier of the newly-created classifier:

!!! abstract "Response body"
    ```json tab="JSON"
    {
        "id": "123-456-abcd-efgh",
        "label": "My new classifier",
        "lastUpdated": "2019-01-01T00:00:00.000Z",
        "editable": true
    } 
  
## Updating classifiers

Similarly, to update the label of an existing classifier, call the following endpoint with the classifier's id field:

<endpoint class="put">/api/classifiers/**{id}**</endpoint>

With a request body such as:

!!! abstract "Request body"
    ```json tab="JSON"
    {
        "label": "New label",
    } 
    ```
    
To set the list of classifiers for an item, make an edit using a `POST` request to (for example, a Data Model):

<endpoint class="put">/api/dataModels/**{datamodelId}**/</endpoint>

!!! abstract "Request body"
    ```json tab="JSON"
        {
            "classifiers": [
                {
                    "id": "156dd4f6-80c7-46d5-98a1-875f917a5dd7"
                }
            ]
        }
    ```

Similarly, all classifiers can be removed from an item by:

<endpoint class="put">/api/dataModels/**{datamodelId}**/</endpoint>

!!! abstract "Request body"
    ```json tab="JSON"
        {
            "classifiers": [
            ]
        }
    ```

A shortcut exists for creating a new classifier on an existing catalogue item: 

<endpoint class="post">/api/features/**{featureComponentId}**/classifiers</endpoint>


!!! abstract "Request body"
    ```json tab="JSON"
        {
            "label": "New classifier name"
        }
    ```

This will create a new classifier with the label "New classifier name", and add it to the list of classifiers of the 
given catalogue item.

    
## Deleting classifiers
    
To delete an existing classifier by its identifier, call the `DELETE` method:    

<endpoint class="delete">/api/classifiers/**{id}**</endpoint>


# Sharing

The permissions on classifiers may be altered using the following endpoints.  Please see the descriptions on 
[Catalogue Items](catalogue-item.md#permissions) for more information about how these endpoints work: 

<endpoint class="delete">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="put">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="delete">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>
<endpoint class="put">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>
<endpoint class="delete">/api/features/**{featureComponentId}**/classifiers/**{id}**</endpoint>


<endpoint class="put">/api/classifiers/**{classifierId}**/**{type}**/**{share}**/**{shareId}**?</endpoint>
<endpoint class="delete">/api/classifiers/**{classifierId}**/**{type}**/**{share}**/**{shareId}**</endpoint>

