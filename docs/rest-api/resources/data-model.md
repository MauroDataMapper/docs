## Data Model object description

In its simplest form, a DataModel can be represented as follows:

```json tab="JSON"
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

The 'hierarchy' endpoint provides 

<endpoint class="get">/api/dataModels/**{dataModelId}**/hierarchy</endpoint>

<endpoint class="get">/api/dataModels/types</endpoint>

## Create data model

<endpoint class="put">/api/dataModels/**{dataModelId}**/newVersion</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/newDocumentationVersion</endpoint>


## Update data model


### 
<endpoint class="put">/api/dataModels/**{dataModelId}**/finalise</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>


## Delete data model
 
## Import / export a data model

<endpoint class="post">/api/dataModels/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>
<endpoint class="post">/api/dataModels/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>



<endpoint class="put">/api/folders/**{folderId}**/dataModels/**{dataModelId}**</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/suggestLinks/**{otherDataModelId}**</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/diff/**{otherDataModelId}**</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/folder/**{folderId}**</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>
<endpoint class="post">/api/dataModels</endpoint>
<endpoint class="get">/api/dataModels</endpoint>
<endpoint class="delete">/api/dataModels</endpoint>
<endpoint class="delete">/api/dataModels/**{id}**</endpoint>
<endpoint class="put">/api/dataModels/**{id}**</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/**{type}**/**{share}**/**{shareId}**?</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/**{type}**/**{share}**/**{shareId}**</endpoint>

