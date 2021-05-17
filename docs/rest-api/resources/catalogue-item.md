A _Catalogue Item_ in the catalogue is an abstract class containing properties that are common to most objects in the catalogue - for example 
DataModels, DataClasses, DataElements, DataTypes, EnumerationValues, Terminologies, etc.  These properties include _metadata (properties)_, _summary 
metadata_, _permissions_, _annotations (comments)_ and so on.  In some cases the url for each endpoint uses the word 'facet'; in others the data 
type (DataModel, DataClass, etc) are used.  This page lists all the endpoints and describes the structure of each property. 



## Metadata

The _metadata_, or _properties_, of a Catalogue Item are extensible key/value pairs to store any further information about an object - including 
technical properies, or field conforming to an external model.  A single item of metadata is structured as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "c9a36d30-2c6a-4dd0-a792-a337a2eca9c8",
        "namespace": "ox.softeng.metadatacatalogue.dataloaders.hdf",
        "key": "Volumes",
        "value": "Varies annually: in 2013/14, 18.2m finished consultant episodes (FCEs) and 15.5m Finished Admission Episodes (FAEs)",
        "lastUpdated": "2019-10-03T09:15:12.082Z"
    }
    ```

The fields are as follows:

- **id** (UUID): The unique identifier of this property
- **namespace** (String): a namespace used to group particular properties - and can be used to filter properties for particular uses
- **key** (String): the title or label of this property.  The combination of **namespace** and **key** should be unique for this object.
- **value** (String): the value that this property holds.  This field may take HTML or MarkDown syntax, and may include links to other objects in 
the catalogue.
- **lastUpdated** (DateTime): The date/time when this Metadata property was last modified

The endpoints for using metadata properties are listed below.

To retrieve all the properties for a particular object, use the following endpoint.  The metadata properties are returned in a [paginated list](../pagination.md) 

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/metadata</endpoint>

Where **{catalogueItemDomainType}** can be one of:

* `folders`,
* `dataModels`,
* `dataClasses`,
* `dataTypes`,
* `terminologies`,
* `terms`, or
* `referenceDataModels`

To get a specific property (whose **id** field is known), use the following endpoint:

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/metadata/**{id}**</endpoint>

To add a new property to an object you have write-access to, post a structure similar to the one displayed above (ignoring **id** and 
**lastUpdated** fields, which will be automatically set to the following endpoint:

<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/metadata</endpoint>

To edit an existing property (whose **id** field is known), use the following endpoint:

<endpoint class="put">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/metadata/**{id}**</endpoint>

To delete an existing property (whose **id** field is known), use the following endpoint:

<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/metadata/**{id}**</endpoint>

The following endpoint returns all known namespaces for a particular object (given by the **id** field).  To find all namespaces across the whole 
catalogue, the final component of the URL can be left off.

<endpoint class="get">/api/metadata/namespaces/**{id}**?</endpoint>



## Permissions

Logged in users may query to discover who is able to read or write a particular object (that they themselves have read-access to).  The structure 
of a response is as follows:

=== "Response body (JSON)"
    ```json
    {
        "readableByEveryone": false,
        "readableByAuthenticated": true,
        "readableByGroups": [],
        "writeableByGroups": [
            {
                "id": "cb1b7f4e-6955-41ba-8f91-2ca92b97c189",
                "label": "Test Group",
                "createdBy": {
                    "id": "dc7a7c25-5622-4cb0-869f-6d0e688b490f",
                    "emailAddress": "joebloggs@test.com",
                    "firstName": "Joe",
                    "lastName": "Bloggs",
                    "userRole": "EDITOR",
                    "disabled": false
                }
            }
        ],
        "readableByUsers": [
            {
                "id": "5e70dbc8-4a1f-4c97-82dd-b05438ba7fae",
                "emailAddress": "joebloggs@test.com",
                "firstName": "Joe",
                "lastName": "Bloggs",
                "userRole": "EDITOR",
                "disabled": false
            }
        ],
        "writeableByUsers": [
            {
                "id": "5e70dbc8-4a1f-4c97-82dd-b05438ba7fae",
                "emailAddress": "joebloggs@test.com",
                "firstName": "Joe",
                "lastName": "Bloggs",
                "userRole": "EDITOR",
                "disabled": false
            }
        ]
    }
    ```

The fields are as follows:

- **readableByEveryone** (Boolean): whether the object in question is publicly available - i.e. can be read by any un-authenticated user of the 
system
- **readableByAuthenticated** (Boolean): whether the object in question can be read by any authenticated (logged-in) user of the system
- **readableByGroups** (Set(Group)): the set of groups who have permission to read a particular object.  The group has a label, an identifier, and 
the details of the user responsible for creating that group
- **writeableByGroups** (Set(Group)): the set of groups who have permission to edit a particular object.  Note that this set of groups is always a 
subset of the groups listed in **readableByGroups**
- **readableByUsers** (Set(User)): the set of users who have permission to read a particular object.  The user has an identifier, first name, last 
name, email address and flag indicating whether their access is currently valid or disabled
- **writeableByGroups** (Set(Group)): the set of users who have permission to edit a particular object.  Note that this set of users is always a 
subset of the users listed in **readableByUsers**

!!! Note
    Note that read/write permissions are propagated through folders and sub-folders, and the list of permissions given is the inferred list.  So 
    changes to that list may not always have an affect if they are contradicted by another assertion further up the tree.


The endpoint for getting the permissions each of DataModel, ReferenceDataModel, Folder, CodeSet and Classifier are listed below.  The details for updating
 permissions are listed on their respective pages. 

<endpoint class="get">/api/dataModels/**{dataModelId}**/permissions</endpoint>
<endpoint class="get">/api/referenceDataModels/**{referenceDataModelId}**/permissions</endpoint>
<endpoint class="get">/api/folders/**{folderId}**/permissions</endpoint>
<endpoint class="get">/api/codeSets/**{codeSetId}**/permissions</endpoint>
<endpoint class="get">/api/classifiers/**{classifierId}**/permissions</endpoint>


## Annotations

Annotations, or comments, can be attached to any item in the catalogue.  The structure is as follows:

=== "Response body (JSON)"
    ```json
    {
        "count": 2,
        "items": [
            {
                "id": "da3d6229-b152-4cbb-8667-eede523c7eb1",
                "description": "DataModel finalised by Joe Bloggs on 2018-09-28T20:21:35.995Z",
                "createdBy": {
                    "id": "5b96991a-d350-4470-958a-29bfac557ed0",
                    "emailAddress": "joebloggs@test.com",
                    "firstName": "Joe",
                    "lastName": "Bloggs",
                    "userRole": "EDITOR",
                    "disabled": false
                },
                "lastUpdated": "2018-09-28T20:21:37.655Z",
                "label": "Finalised Model"
            },
            {
                "id": "670e7c31-00fd-425f-903f-6d024845e63e",
                "createdBy": {
                    "id": "6c02358a-d3e3-4bee-93d5-839ead6a0acd",
                    "emailAddress": "joebloggs@test.com",
                    "firstName": "Joe",
                    "lastName": "Bloggs",
                    "userRole": "EDITOR",
                    "disabled": false
                },
                "lastUpdated": "2018-07-17T15:51:45.643Z",
                "label": "Is this model is ready for finalisation?"
            }
        ]
    }
    ```

### Listing annotations

To get all the annotations for a particular object, use the following endpoint. The results are returned in a [paginated list](../pagination.md)

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations</endpoint>

Where **{catalogueItemDomainType}** can be one of:

* `folders`,
* `dataModels`,
* `dataClasses`,
* `dataTypes`,
* `terminologies`,
* `terms`, or
* `referenceDataModels`

To get the details of a particular annotation / comment, whose **id** is known, use the following endpoint:

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{id}**</endpoint>

To create a new top-level annotation, post to the following endpoint, with a body similar to the JSON above (but without the **id** and
 **lastUpdated** fields)
   
<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations</endpoint>

To delete an annotation / comment whose identifier is known, use the following _delete_ endpoint:

<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{id}**</endpoint>

### Child annotations (responses)

Comments can have child comments (or replies).  To get all the child comments for a particular comment, use the following endpoint. The
 results are returned in a [paginated list](../pagination.md)

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{annotationId}**/annotations</endpoint>

To get the details of a particular child annotation / comment, whose **id** is known, use the following endpoint:

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{annotationId}**/annotations/**{id}**</endpoint>

To create a new child annotation, post to the following endpoint, with a body similar to the JSON above (but without the **id** and
 **lastUpdated** fields)

<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{annotationId}**/annotations</endpoint>

To delete a child annotation / comment whose identifier is known, use the following _delete_ endpoint:

<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/annotations/**{annotationId}**/annotations/**{id}**</endpoint>
 

## Searching

An advanced search is powered by Lucene.  The parameters for an advanced search can be provided as query parameters of a _get_ request, as follows:

| Parameter | Description |
|-----------|-------------|
| `searchTerm` | (String): the search string - this can take a number of standard search operators - for example "smoking + pregnancy" |
| `limit` | (Integer): the number of results returned in a [paginated list](../pagination.md) |
| `offset` | (Integer): the index of the first result returned in a [paginated list](../pagination.md) |
| `domainTypes` | (Set(String)): the catalogue object types that should be searched. These can include: `DataModel`, `DataClass`, `DataElement`, `DataType`, `EnumerationType`. |
| `labelOnly` | (Boolean): whether the search should only query the label of all objects |
| `dataModelTypes` | (Set(String)): the types of data model that should be searched - for example `Data Asset`, `Data Standard` |
| `classifiers` | (Set(String)): a set of classifier labels, such that all results must be classified by one of those tags |
| `lastUpdatedAfter` | (DateTime): Only include objects in the search results if they have been modified more recently than the given date |
| `lastUpdatedBefore` | (DateTime): Only include objects in the search results if they have been modified earlier than the given date  |
| `createdAfter` | (DateTime): Only include objects in the search results if they were created more recently than the given date |
| `createdBefore` | (DateTime): Only include objects in the search results if they were created earlier than the given date |

The response will be a [paginated list](../pagination.md) of items, where each item has the following structure:

=== "Response body (JSON)"
    ```json 
    {
        "id": "127bdf61-cbfe-47dc-9854-fdce276f13bf",
        "domainType": "DataElement",
        "label": "AGE AT ONSET OF SYMPTOMS (CHILDREN TEENAGERS AND YOUNG ADULTS CANCER)",
        "description": "AGE BAND AT SMOKING QUIT DATE is derived as the number of completed years between the PERSON BIRTH DATE of the PERSON and the SMOKING QUIT DATE of the Person Stop Smoking Episode.  Permitted National Codes:  01  Under 18 years of age  02  18 to 34 years of age  03  35 - 44 years of age  04  45 - 59 years of age  05  60 and over years of age",
        "breadcrumbs": [
            {
                "id": "078955c7-6c0f-4fc2-a30e-55629a85b9da",
                "label": "NHS Data Dictionary",
                "domainType": "DataModel",
                "finalised": true
            },
            {
                "id": "012e8dd5-b4b1-4d26-82aa-17430baf2e2b",
                "label": "All Data Elements",
                "domainType": "DataClass"
            }
        ]
    }
    ```
where the fields are defined as follows:

- **id** (UUID): The identifier of the returned object
- **domainType** (String): The type of the returned object - for example "DataModel", "DataClass", "DataElement"
- **label** (String): The name of the returned object
- **description** (String): The description of the returned object.  This may include formatting specified in HTML, or MarkDown.
- **breadcrumbs** (List(Breadcrumb)): An ordered list of, e.g. DataModels and DataClasses to show the location of an object in the hierarchy of a
 model.  This will include, for each component of the breadcrumb, an **id**, a **label** and a **domainType**.  

To search across the whole catalogue, use the following endpoint, optionally passing the above query parameters:
 
<endpoint class="get">/api/tree/folders/search</endpoint>

Similarly, to search within a particular data model, use the following:

<endpoint class="post">/api/dataModels/**{dataModelId}**/search</endpoint>

Finally, to search within a specific Data Class, use the following:

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/search</endpoint>


## Item history

The edit history for various catalogue items can be retrieved using the endpoints listed below.  The format of a response is a paginated list of
 edits, with the following structure:

=== "Response body (JSON)"
    ```json
    {
        "dateCreated": "2018-07-17T15:53:17.276Z",  
        "createdBy": {
            "id": "6c02358a-d3e3-4bee-93d5-839ead6a0acd",
            "emailAddress": "ollie.freeman@gmail.com",
            "firstName": "Oliver",
            "lastName": "Freeman",
            "userRole": "EDITOR",
            "disabled": false
        }
        "description": "[Data Standard:HIC: Hepatitis v2.0.0] changed properties [folder]"
    }
    ```

The fields have the following definition:

- **dateCreated** (DateTime): the date and time when this modification was made
- **createdBy** (User): the user responsible for making the edit.  This will include their **id**, **emailAddress**, **firstName**, **lastName
**, **userRole** and whether the user account is currently **disabled**.  It may also include the profile image of the user in question
- **description** (String): The human-readable description of the edit made.  These descriptions are automatically generated by the catalogue 
 
The endpoints for getting the edit history for each of DataModel, Terminology, Folder, CodeSet, Classifier and UserGroup are listed below. 

<endpoint class="get">/api/dataModels/**{dataModelId}**/edits</endpoint>
<endpoint class="get">/api/terminologies/**{terminologyId}**/edits</endpoint>
<endpoint class="get">/api/folders/**{folderId}**/edits</endpoint>
<endpoint class="get">/api/codeSets/**{codeSetId}**/edits</endpoint>
<endpoint class="get">/api/classifiers/**{classifierId}**/edits</endpoint>
<endpoint class="get">/api/userGroups/**{userGroupId}**/edits</endpoint>


## Reference files

Reference files (or attachments) can be stored alongside various catalogue items to supplement information about the catalogue item. Reference 
files have the following structure:

=== "Response body (JSON)"
    ```json
    {
        "id": "eea67c19-1833-4125-9934-b06f45844c20",
        "domainType": "ReferenceFile",
        "fileName": "uploadedFile.png",
        "fileSize": 80899,
        "fileType": "image/png",
        "lastUpdated": "2021-05-13T12:50:37.523Z"
    }
    ```

The fields have the following definition:

- **id** (UUID): The identifier of the returned object
- **domainType** (String): The type of the returned object - in this case, "ReferenceFile"
- **fileName** (String): The name of the uploaded file
- **fileSize** (Number): The size of the uploaded reference file, in bytes
- **fileType** (String): The MIME type of the uploaded reference file
- **lastUpdated** (DateTime): the date and time when this modification was made

To upload and attach a new reference file to a catalogue item, use the following endpoint and request payload:

<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/referenceFiles</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "fileName": "uploadedFile.png",
        "fileSize": 80899,
        "fileType": "image/png",
        "fileContents": [ 
            // Array of bytes
        ]
    }
    ```

Where **{catalogueItemDomainType}** can be one of:

* `dataModels`,
* `terminologies`,
* `codeSets`, or
* `referenceDataModels`

To get either a [paginated list](../pagination.md) of reference files for a catalogue item, or an individual reference file known by **{id}**:

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/referenceFiles</endpoint>
<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/referenceFiles/**{id}**</endpoint>

To delete a reference file from a catalogue item whose identifier is known, use the following delete endpoint:

<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/referenceFiles/**{id}**</endpoint>

## Summary Metadata

<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata</endpoint>
<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata</endpoint>
<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{id}**</endpoint>
<endpoint class="put">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{id}**</endpoint>
<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{id}**</endpoint>

### Summary Metadata Reports

<endpoint class="post">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports</endpoint>
<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports</endpoint>
<endpoint class="delete">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>
<endpoint class="put">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>
<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>


