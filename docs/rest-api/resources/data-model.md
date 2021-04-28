## DataModel object description

In its simplest form, a DataModel can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "DataModel",
        "label": "Diagnostic Imaging Dataset",
        "aliases": [
            "DID"
        ],
        "description": "Central collection of detailed information about diagnostic imaging tests carried out on NHS patients (such as x-rays and MRI scans).  Any organisation providing diagnostic imaging tests to NHS patients in England, i.e.:\n* NHS (Foundation) trusts / hospitals\n* NHS-funded activity with independent sector providers\nNOT included are breast screening services or any other diagnostic imaging tests not typically recorded on the local provider's Radiology Information Systems.\nDiagnostic Imaging Dataset (DID) does not store the images themselves, or the outcomes/diagnoses related to these images.",
        "author": "NHS Digital",
        "organisation": "NHS Digital",
        "editable": true,
        "documentationVersion": "2.0.0",
        "lastUpdated": "2019-10-03T12:00:05.95Z",
        "classifiers": [
            {
                "id": "2fd9e8c7-4545-42f4-99a3-f93f14d35786",
                "label": "NIHR Health Data Finder",
                "lastUpdated": "2019-10-03T09:15:37.323Z"
            }
        ],
        "type": "Data Asset",
        "finalised": false,
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this data model
- **domainType** (Type): The domain type of this catalogue object - always "DataModel" in this case
- **label** (String): The human-readable identifier of this model.  The combination of label and documentationVersion are unique across the catalogue
- **aliases** (Set(String)): Any other names by which this datamodel is known
- **description** (String): A long description of the data model, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **author** (String): The names of those creating and maintaining this Datamodel (not any underlying dataset itself)
- **organisation** (String): The name of the organisation holding the dataset
- **editable** (Boolean): Whether the current user (see [authentication](../authentication.md)) is allowed to edit this DataModel
- **documentationVersion** (Version): The version of the description of an underlying dataset
- **lastUpdated** (DateTime): The date/time when this DataModel was last modified
- **classifiers** (Set(Classifier)): The **id**, **label** and **lastUpdated** date of any classifiers used to tag or categorise this data model 
(see [classifiers](classifier.md))
- **type** (DataModel Type): Whether this DataModel is a "Data Asset", or a "Data Standard"
- **finalised** (Boolean): Whether this DataModel has been 'finalised', or is in draft mode

Endpoints which return multiple models typically include sufficient fields for generating links on the interface - a separate call to return the 
details of the DataModel is usually required. 

As well as the endpoints listed below, a DataModel is also a CatalogueItem, and so a DataModel identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)



## List all data models

The following endpoint returns a [paginated](../pagination.md) list of all DataModel objects readable by the current user:  

<endpoint class="get">/api/dataModels</endpoint>

This endpoint returns all the DataModels within a particular folder; again, this result is [paginated](../pagination.md).

<endpoint class="get">/api/folders/**{folderId}**/dataModels</endpoint>


## Get information about a particular data model

This endpoint provides the default information about a DataModel, as per the JSON at the top of the page.

<endpoint class="get">/api/dataModels/**{id}**</endpoint>

The 'hierarchy' endpoint provides a structured representation of the entire datamodel - child DataClasses, sub-DataClasses, and their child
 DataElements.   

!!! Warning 
    This call can take a long time for large data models

<endpoint class="get">/api/dataModels/**{dataModelId}**/hierarchy</endpoint>

The 'types' endpoint lists all the datatypes for a given datamodel.  This returns primitive, reference, enumeration and terminology types owned by
 the data model, whether used or not.

<endpoint class="get">/api/dataModels/types</endpoint>

## Create data model

To create a new data model from scratch, use the following _post_ endpoint.  Within the body of this call, you should include a folder identifier.

<endpoint class="post">/api/dataModels</endpoint>

There are two ways of versioning Data Models in the catalogue.  To create an entirely new version of a model, please use the following endpoint:

<endpoint class="put">/api/dataModels/**{dataModelId}**/newModelVersion</endpoint>

The name must be different to the original model.

To create a new 'documentation version', use the following endpoint:

<endpoint class="put">/api/dataModels/**{dataModelId}**/newDocumentationVersion</endpoint>

By default, this will supersede the original data model.

It is also possible to _branch_ and _fork_ Data Models to create drafts before finalising them. To create a new _branch_ from an existing Data Model:

<endpoint class="put">/api/dataModels/**{dataModelId}**/newBranchModelVersion</endpoint>

To create a _fork_ of the original data model:

<endpoint class="put">/api/dataModels/**{dataModelId}**/newForkModel</endpoint>
## Update data model

To edit the primitive properties of a data model, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/dataModels/**{id}**</endpoint>

To move a data model from one folder to another, call the following, using the id fields for the data model, and the new folder:

<endpoint class="put">/api/folders/**{folderId}**/dataModels/**{dataModelId}**</endpoint>

Alternatively, you can call this equivalent endpoint:

<endpoint class="put">/api/dataModels/**{dataModelId}**/folder/**{folderId}**</endpoint>

To move a data model from a draft state to 'finalised', use the following endpoint:

<endpoint class="put">/api/dataModels/**{dataModelId}**/finalise</endpoint>

### Sharing

To allow a model to be read by any authenticated user of the system, use the following endpoint:

<endpoint class="put">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>

... and to remove this flag, use the following:

<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>

Similarly, to allow the model to be publicly readable - ie. readable by any unauthenticated user of the system, 
use the following endpoint: 

<endpoint class="put">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>

... and the following to remove this flag:

<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>


## Delete data model

To delete a data model, use the following endpoint.  The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete
 is used if the user is an administrator.
 
<endpoint class="delete">/api/dataModels/**{id}**?permanent=**{true/false}**</endpoint>

 
## Import / export a data model

To export a data model using a particular export plugin, you will need to know the namespace, the name, and the version of the plugin.  The
 following endpoint can be used to export multiple data models: 

<endpoint class="post">/api/dataModels/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>

To export a single model, you can use the following endpoint with the id of the data model specified:

<endpoint class="get">/api/dataModels/**{dataModelId}**/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>


Similarly, to import one or more data models, the namespace, name and version of the import plugin must be known.  The body of this method should
 be the parameters for the import, including any files that are required.

<endpoint class="post">/api/dataModels/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>






