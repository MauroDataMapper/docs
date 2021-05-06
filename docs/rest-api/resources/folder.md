A Folder is a _container_ type and can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "Folder",
        "label": "folder",        
        "description": "Represents a folder.",        
        "lastUpdated": "2021-04-28T10:10:13.945Z",
        "hasChildFolders": true
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this folder
- **domainType** (Type): The domain type of this catalogue object. Will always be `Folder` in this case.
- **label** (String): The human-readable identifier of this folder.
- **description** (String): A long description of the folder, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **lastUpdated** (DateTime): The date/time when this folder was last modified
- **hasChildFolders** (Boolean): Determines if this folder contains child folders.

As well as the endpoints listed below, a Folder is also a CatalogueItem, and so a Folder identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Child Folders

A folder may contain child folders. Endpoints are provided to differentiate between parent and child folders.

## Getting information

The following endpoints returns a [paginated](../pagination.md) list of all the folders. The first requests all root folders in Mauro, the second requests the folders for a parent folder.

<endpoint class="get">/api/folders</endpoint>

<endpoint class="get">/api/folders/**{folderId}**/folders</endpoint>

These endpoints provide the detailed information about a particular folder; the first requests a root folder in Mauro, the second requests a folder from a parent folder.

<endpoint class="get">/api/folders/**{id}**</endpoint>

<endpoint class="get">/api/folders/**{folderId}**/folders/**{id}**</endpoint>

## Create / Update / Delete

To create a new folder from scratch, use the following _post_ endpoints, depending on whether to create one with or without a parent.

<endpoint class="post">/api/folders</endpoint>

<endpoint class="post">/api/folders/**{folderId}**/folders</endpoint>

To edit the properties of a folder, use the following endpoints, with a body similar to the JSON described at the top of this page. Use the appropriate endpoint depending on whether to edit one with or without a parent.

<endpoint class="put">/api/folders/**{id}**</endpoint>

<endpoint class="put">/api/folders/**{folderId}**/folders/**{id}**</endpoint>

To delete a folder, use the following endpoint, depending on whether to delete one with or without a parent. The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete is used if the user is an administrator.

<endpoint class="delete">/api/folders/**{id}**?permanent=**{true/false}**</endpoint>

<endpoint class="delete">/api/folders/**{folderId}**/folders/**{id}**?permanent=**{true/false}**</endpoint>

## Security

<endpoint class="delete">/api/folders/**{folderId}**/readByAuthenticated</endpoint>
<endpoint class="put">/api/folders/**{folderId}**/readByAuthenticated</endpoint>
<endpoint class="delete">/api/folders/**{folderId}**/readByEveryone</endpoint>
<endpoint class="put">/api/folders/**{folderId}**/readByEveryone</endpoint>
