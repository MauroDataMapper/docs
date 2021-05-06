In its simplest form, a Code Set can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "CodeSet",
        "label": "Sample Codeset",
        "aliases": [
            "sample"
        ],
        "description": "Example of a Codeset",
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
        "type": "CodeSet",
        "finalised": false,
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this code set
- **domainType** (Type): The domain type of this catalogue object - always `CodeSet` in this case
- **label** (String): The human-readable identifier of this code set.  The combination of `label` and `documentationVersion` are unique across the catalogue
- **aliases** (Set(String)): Any other names by which this code set is known
- **description** (String): A long description of the code set, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **author** (String): The names of those creating and maintaining this code set (not any underlying dataset itself)
- **organisation** (String): The name of the organisation holding the dataset
- **documentationVersion** (Version): The version of the description of an underlying dataset
- **lastUpdated** (DateTime): The date/time when this code set was last modified
- **classifiers** (Set(Classifier)): The **id**, **label** and **lastUpdated** date of any classifiers used to tag or categorise this code set 
(see [classifiers](classifier.md))
- **type** (CodeSet Type): Will always be defined as `CodeSet`.
- **finalised** (Boolean): Whether this code set has been 'finalised', or is in draft mode

Endpoints which return multiple code sets typically include sufficient fields for generating links on the interface - a separate call to return the 
details of the Code Set is usually required. 

As well as the endpoints listed below, a Code Set is also a CatalogueItem, and so a Code Set identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)


## List all code sets

The following endpoint returns a [paginated](../pagination.md) list of all code set objects readable by the current user:  

<endpoint class="get">/api/codeSets</endpoint>

This endpoint returns all the code sets within a particular folder; again, this result is [paginated](../pagination.md).

<endpoint class="get">/api/folders/**{folderId}**/codeSets</endpoint>


## Get information about a particular code set

This endpoint provides the default information about a code set, as per the JSON at the top of the page.

<endpoint class="get">/api/codeSets/**{id}**</endpoint>

## Create code set

To create a new code set from scratch, use the following _post_ endpoint.  Within the body of this call, you should include a folder identifier.

<endpoint class="post">/api/codeSets</endpoint>

There are two ways of versioning code set in the catalogue.  To create an entirely new version of a model, please use the following endpoint:

<endpoint class="put">/api/codeSets/**{codeSetId}**/newModelVersion</endpoint>

The name must be different to the original model.

To create a new 'documentation version', use the following endpoint:

<endpoint class="put">/api/codeSets/**{codeSetId}**/newDocumentationVersion</endpoint>

By default, this will supersede the original data model.

It is also possible to _branch_ and _fork_ code sets to create drafts before finalising them. To create a new _branch_ from an existing code set:

<endpoint class="put">/api/codeSets/**{codeSetId}**/newBranchModelVersion</endpoint>

To create a _fork_ of the original data model:

<endpoint class="put">/api/codeSets/**{codeSetId}**/newForkModel</endpoint>

## Update code set

To edit the primitive properties of a code set, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/codeSets/**{id}**</endpoint>

To move a code set from one folder to another, call the following, using the id fields for the code set, and the new folder:

<endpoint class="put">/api/folders/**{folderId}**/codeSets/**{codeSetId}**</endpoint>

Alternatively, you can call this equivalent endpoint:

<endpoint class="put">/api/codeSets/**{codeSetId}**/folder/**{folderId}**</endpoint>

To move a code set from a draft state to 'finalised', use the following endpoint:

<endpoint class="put">/api/codeSets/**{codeSetId}**/finalise</endpoint>

### Sharing

To allow a code set to be read by any authenticated user of the system, use the following endpoint:

<endpoint class="put">/api/codeSets/**{codeSetId}**/readByAuthenticated</endpoint>

... and to remove this flag, use the following:

<endpoint class="delete">/api/codeSets/**{codeSetId}**/readByAuthenticated</endpoint>

Similarly, to allow the code set to be publicly readable - ie. readable by any unauthenticated user of the system, 
use the following endpoint: 

<endpoint class="put">/api/codeSets/**{codeSetId}**/readByEveryone</endpoint>

... and the following to remove this flag:

<endpoint class="delete">/api/codeSets/**{codeSetId}**/readByEveryone</endpoint>


## Delete code set

To delete a code set, use the following endpoint.  The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete
 is used if the user is an administrator.
 
<endpoint class="delete">/api/codeSets/**{id}**?permanent=**{true/false}**</endpoint>

An administrator is able to restore a 'soft' deleted code set using the following endpoint:

<endpoint class="put">/api/admin/codeSets/**{id}**/undoSoftDelete</endpoint>
 
## Import / export a code set

To export a code set using a particular export plugin, you will need to know the namespace, the name, and the version of the plugin.  The
 following endpoint can be used to export multiple code sets: 

<endpoint class="post">/api/codeSets/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>

To export a single code set, you can use the following endpoint with the id of the code sets specified:

<endpoint class="get">/api/codeSets/**{codeSetId}**/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>


Similarly, to import one or more code sets, the namespace, name and version of the import plugin must be known.  The body of this method should
 be the parameters for the import, including any files that are required.

<endpoint class="post">/api/codeSets/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>
