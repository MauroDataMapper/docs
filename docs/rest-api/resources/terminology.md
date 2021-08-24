In its simplest form, a Terminology can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "Terminology",
        "label": "Sample Terminology",
        "aliases": [
            "sample"
        ],
        "description": "Example of a Terminology",
        "author": "NHS Digital",
        "organisation": "NHS Digital",
        "documentationVersion": "2.0.0",
        "lastUpdated": "2019-10-03T12:00:05.95Z",
        "classifiers": [
            {
                "id": "2fd9e8c7-4545-42f4-99a3-f93f14d35786",
                "label": "NIHR Health Data Finder",
                "lastUpdated": "2019-10-03T09:15:37.323Z"
            }
        ],
        "type": "Terminology",
        "finalised": false,
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this terminology
- **domainType** (Type): The domain type of this catalogue object - always `Terminology` in this case
- **label** (String): The human-readable identifier of this terminology.  The combination of `label` and `documentationVersion` are unique across the catalogue
- **aliases** (Set(String)): Any other names by which this terminology is known
- **description** (String): A long description of the description, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **author** (String): The names of those creating and maintaining this terminology (not any underlying dataset itself)
- **organisation** (String): The name of the organisation holding the terminology
- **documentationVersion** (Version): The version of the description of an underlying dataset
- **lastUpdated** (DateTime): The date/time when this terminology was last modified
- **classifiers** (Set(Classifier)): The **id**, **label** and **lastUpdated** date of any classifiers used to tag or categorise this terminology 
(see [classifiers](classifier.md))
- **type** (Terminology Type): Will always be defined as `Terminology`.
- **finalised** (Boolean): Whether this terminology has been 'finalised', or is in draft mode

Endpoints which return multiple terminologies typically include sufficient fields for generating links on the interface - a separate call to return the 
details of the terminology is usually required. 

As well as the endpoints listed below, a terminology is also a CatalogueItem, and so a terminology identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)


## List all terminologies

The following endpoint returns a [paginated](../pagination.md) list of all terminologies readable by the current user:  

<endpoint class="get">/api/terminologies</endpoint>

This endpoint returns all the terminologies within a particular folder; again, this result is [paginated](../pagination.md).

<endpoint class="get">/api/folders/**{folderId}**/terminologies</endpoint>


## Get information about a particular terminology

This endpoint provides the default information about a terminology, as per the JSON at the top of the page.

<endpoint class="get">/api/terminologies/**{id}**</endpoint>

## Create terminologies

There are two ways of versioning terminologies in the catalogue.  To create an entirely new version of a model, please use the following endpoint:

<endpoint class="put">/api/terminology/**{terminologyId}**/newBranchModelVersion</endpoint>

The name must be different to the original model.

To create a new 'documentation version', use the following endpoint:

<endpoint class="put">/api/terminology/**{terminologyId}**/newDocumentationVersion</endpoint>

By default, this will supersede the original terminology.

It is also possible to _branch_ and _fork_ code sets to create drafts before finalising them. To create a new _branch_ from an existing code set:

<endpoint class="put">/api/terminology/**{terminologyId}**/newBranchModelVersion</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "branchName": "newBranch"
    }
    ```

To create a _fork_ of the original terminology:

<endpoint class="put">/api/terminology/**{terminologyId}**/newForkModel</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "label": "newForkLabel"        
    }
    ```

## Update terminology

To edit the primitive properties of a terminology, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/terminology/**{id}**</endpoint>

To move a terminology from one folder to another, call the following, using the id fields for the terminology, and the new folder:

<endpoint class="put">/api/folders/**{folderId}**/terminologies/**{terminologyId}**</endpoint>

Alternatively, you can call this equivalent endpoint:

<endpoint class="put">/api/terminologies/**{terminologyId}**/folder/**{folderId}**</endpoint>

To move a terminology from a draft state to 'finalised', use the following endpoint:

<endpoint class="put">/api/terminologies/**{terminologyId}**/finalise</endpoint>

### Sharing

To allow a terminology to be read by any authenticated user of the system, use the following endpoint:

<endpoint class="put">/api/terminologies/**{terminologyId}**/readByAuthenticated</endpoint>

... and to remove this flag, use the following:

<endpoint class="delete">/api/terminologies/**{terminologyId}**/readByAuthenticated</endpoint>

Similarly, to allow the terminology to be publicly readable - ie. readable by any unauthenticated user of the system, 
use the following endpoint: 

<endpoint class="put">/api/terminologies/**{terminologyId}**/readByEveryone</endpoint>

... and the following to remove this flag:

<endpoint class="delete">/api/terminologies/**{terminologyId}**/readByEveryone</endpoint>


## Delete terminology

To delete a terminology, use the following endpoint.  The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete
 is used if the user is an administrator.
 
<endpoint class="delete">/api/terminologies/**{id}**?permanent=**{true/false}**</endpoint>

An administrator is able to restore a 'soft' deleted terminology using the following endpoint:

<endpoint class="put">/api/admin/terminologies/**{id}**/undoSoftDelete</endpoint>
 
## Import / export a terminology

To export a terminology using a particular export plugin, you will need to know the namespace, the name, and the version of the plugin.  The
 following endpoint can be used to export multiple code sets: 

<endpoint class="post">/api/terminologies/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>

To export a single terminology, you can use the following endpoint with the id of the terminologies specified:

<endpoint class="get">/api/terminologies/**{terminologyId}**/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>


Similarly, to import one or more terminologies, the namespace, name and version of the import plugin must be known.  The body of this method should
 be the parameters for the import, including any files that are required.

<endpoint class="post">/api/terminologies/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>
