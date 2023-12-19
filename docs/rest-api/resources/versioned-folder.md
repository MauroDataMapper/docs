## Description

A Versioned Folder is a container type and can be represented as a mixture of a [Folder](folder.md) and a [Data Model](data-model.md), since it shares the functional characteristics of both - a container for holding other catalogue items, and a model that can be version controlled.

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "VersionedFolder",
        "label": "Sample Versioned Folder",
        "aliases": [
            "SVF"
        ],
        "description": "First sample version controlled folder.",        
        "branchName": "main",
        "documentationVersion": "2.0.0",
        "modelVersion": "2.0.0"
        "lastUpdated": "2019-10-03T12:00:05.95Z",
        "classifiers": [
            {
                "id": "2fd9e8c7-4545-42f4-99a3-f93f14d35786",
                "label": "Samples",
                "lastUpdated": "2019-10-03T09:15:37.323Z"
            }
        ],
        "finalised": true,
        "hasChildFolders": true
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this versioned folder.
- **domainType** (Type): The domain type of this catalogue object - always "VersionedFolder" in this case
- **label** (String): The human-readable identifier of this folder.  The combination of label and documentationVersion are unique across the catalogue
- **aliases** (Set(String)): Any other names by which this versioned folder is known
- **description** (String): A long description of the versioned folder, and any important characteristics of the folder contents.  This field may include HTML, or 
MarkDown.
- **documentationVersion** (Version): The version of the description of an underlying versioned folder.
- **modelVersion** (Version): The version of the folder of an underlying versioned folder.
- **lastUpdated** (DateTime): The date/time when this Versioned Folder was last modified
- **classifiers** (Set(Classifier)): The **id**, **label** and **lastUpdated** date of any classifiers used to tag or categorise this versioned folder 
(see [classifiers](classifier.md))
- **finalised** (Boolean): Whether this Versioned Folder has been 'finalised', or is in draft mode
- **hasChildFolders** (Boolean): Determines if this folder contains child folders.

Endpoints which return multiple versioned folders typically include sufficient fields for generating links on the interface - a separate call to return the 
details of the Versioned Folder is usually required. 

As well as the endpoints listed below, a Versioned Folder is also a CatalogueItem, and so a Versioned Folder identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)


## Getting information

The following endpoint returns a [paginated](../pagination.md) list of all versioned folders readable by the current user:  

<endpoint class="get">/api/versionedFolders</endpoint>

This endpoint returns all the Versioned Folders within a particular folder; again, this result is [paginated](../pagination.md).

<endpoint class="get">/api/folders/**{folderId}**/versionedFolders</endpoint>

This endpoint provides the default information about a Versioned Folder, as per the JSON at the top of the page.

<endpoint class="get">/api/versionedFolders/**{id}**</endpoint>

## Create versioned folder

To create a new versioned folder from scratch, use the following _post_ endpoint.  Within the body of this call, you should include a folder identifier.

<endpoint class="post">/api/versionedFolder</endpoint>

There are two ways of versioning Versioned Folders in the catalogue.  To create an entirely new version of an existing folder, please use the following endpoint with no request body:

<endpoint class="put">/api/versionedFolders/**{id}**/newBranchModelVersion</endpoint>

The name must be different to the original folder.

To create a new 'documentation version', use the following endpoint:

<endpoint class="put">/api/versionedFolders/**{id}**/newDocumentationVersion</endpoint>

By default, this will supersede the original versioned folder.

It is also possible to _branch_ and _fork_ Versioned Folders to create drafts before finalising them. To create a new _branch_ from an existing Versioned Folder:

<endpoint class="put">/api/versionedFolders/**{id}**/newBranchModelVersion</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "branchName": "newBranch"
    }
    ```

To create a _fork_ of the original versioned folder:

<endpoint class="put">/api/versionedFolders/**{id}**/newForkModel</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "label": "newForkLabel"        
    }
    ```

## Update versioned folder

To edit the primitive properties of a versioned folder, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/versionedFolders/**{id}**</endpoint>

To move a versioned folder from one folder to another, call the following, using the id fields for the versioned folder, and the new folder:

<endpoint class="put">/api/folders/**{folderId}**/versionedFolders/**{id}**</endpoint>

Alternatively, you can call this equivalent endpoint:

<endpoint class="put">/api/versionedFolders/**{id}**/folder/**{folderId}**</endpoint>

## Sharing

To allow a versioned folder to be read by any authenticated user of the system, use the following endpoint:

<endpoint class="put">/api/versionedFolders/**{id}**/readByAuthenticated</endpoint>

... and to remove this flag, use the following:

<endpoint class="delete">/api/versionedFolders/**{id}**/readByAuthenticated</endpoint>

Similarly, to allow the versioned folder to be publicly readable - ie. readable by any unauthenticated user of the system, 
use the following endpoint: 

<endpoint class="put">/api/versionedFolders/**{id}**/readByEveryone</endpoint>

... and the following to remove this flag:

<endpoint class="delete">/api/versionedFolders/**{id}**/readByEveryone</endpoint>


## Delete versioned folder

To delete a versioned folder, use the following endpoint.  The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete
 is used if the user is an administrator.
 
<endpoint class="delete">/api/versionedFolders/**{id}**?permanent=**{true/false}**</endpoint>

An administrator is able to restore a 'soft' deleted code set using the following endpoint:

<endpoint class="put">/api/admin/versionedFolders/**{id}**/undoSoftDelete</endpoint>


## Finalise a versioned folder

To _finalise_ a versioned folder means to lock it to a particular version and make it read-only; only new versions can be created to make further modifications after that point. This also applies to the child contents of this versioned folder too, all child items will share the same finalised state and version number assigned. Use this endpoint with a similar payloads described below to finalise a versioned folder.

<endpoint class="put">/api/versionedFolders/**{id}**/finalise</endpoint>

To automatically let Mauro choose the next version number, set the **versionChangeType** property to either `'Major'`, `'Minor'` or `'Patch'`.

=== "Request body (JSON)"
    ```json
    {
        "versionChangeType": "Major" | "Minor" | "Patch"
    }
    ```

Mauro uses [Semantic Versioning](https://semver.org/) rules to determine the next appropriate version number based on the **versionChangeType** value provided.

To optionally choose your own version number, provide this payload. If **versionChangeType** is `'Custom'`, then **version** must also be provided.

=== "Request body (JSON)"
    ```json
    {
        "versionChangeType": "Custom",
        "version": "1.2.3.4"
    }
    ```

In all cases you may also supply an optional _tag name_ to assign with the finalised version to help provide more context, as follows:

=== "Request body (JSON)"
    ```json
    {
        "versionChangeType": "Major" | "Minor" | "Patch",
        "versionTag": "My first version"
    }
    ```

## Merging versioned folders

If [creating branches](#create-versioned-folder) of versioned folders, it is possible to merge the data values from one versioned folder to another. The first step is to calculate the _differences_ between two versioned folders, as follows:

<endpoint class="get">/api/versionedFolders/**{sourceId}**/mergeDiff/**{targetId}**?isLegacy=false</endpoint>

=== "Response body (JSON)"
    ```json
    {
        "sourceId": "f9a4e390-6259-4616-b725-d45524851a82",
        "targetId": "f5841f3f-7a63-4aa2-9c72-a64305d44dcf",
        "path": "vf:Model Version Tree Folder$interestingBranch",
        "label": "Model Version Tree Folder",
        "count": 6,
        "diffs": [            
            {
                "path": "vf:Model Version Tree Folder$interestingBranch|ann:Test Comment",
                "isMergeConflict": false,
                "isSourceModificationAndTargetDeletion": false,
                "type": "creation"
            },
            {
                "path": "vf:Model Version Tree Folder$interestingBranch|dm:Test Data Model",
                "isMergeConflict": false,
                "isSourceModificationAndTargetDeletion": false,
                "type": "creation"
            },
            {
                "path": "vf:Model Version Tree Folder$interestingBranch|md:v1Versioning.com.mdk1",
                "isMergeConflict": false,
                "isSourceDeletionAndTargetModification": false,
                "type": "deletion"
            },
            {
                "fieldName": "value",
                "path": "vf:Model Version Tree Folder$interestingBranch|md:org.datacite.creator@value",
                "sourceValue": "Peter Monks",
                "targetValue": "Mauro Administrator",
                "commonAncestorValue": null,
                "isMergeConflict": true,
                "type": "modification"
            },
            {
                "fieldName": "value",
                "path": "vf:Model Version Tree Folder$interestingBranch|md:test.com.testProperty@value",
                "sourceValue": "Oliver Freeman",
                "targetValue": "Peter Monks",
                "commonAncestorValue": null,
                "isMergeConflict": true,
                "type": "modification"
            },
            {
                "path": "vf:Model Version Tree Folder$interestingBranch|ru:Bootstrapped versioning V2Model Rule|rr:sql",
                "isMergeConflict": false,
                "isSourceModificationAndTargetDeletion": false,
                "type": "creation"
            }
        ]
    }
    ```

The **diffs** collection will hold each change found between the two versioned folders and how they relate.

All changes need to be manually organised into _patches_ so that they can be applied to the target versioned folder. Then the following endpoint is used to commit:

<endpoint class="put">/api/versionedFolders/**{sourceId}**/mergeInto/**{targetId}**?isLegacy=false</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "changeNotice": "Change comment",
        "deleteBranch": false,
        "patch": {
            "sourceId": "f9a4e390-6259-4616-b725-d45524851a82",
            "targetId": "f5841f3f-7a63-4aa2-9c72-a64305d44dcf",
            "label": "Model Version Tree Folder",
            "count": 4,
            "patches": [
                {
                    "path": "vf:Model Version Tree Folder$interestingBranch|ru:Bootstrapped versioning V2Model Rule|rr:sql",
                    "isMergeConflict": false,
                    "isSourceModificationAndTargetDeletion": false,
                    "type": "creation"
                },
                {
                    "fieldName": "description",
                    "path": "vf:Model Version Tree Folder$interestingBranch@description",
                    "sourceValue": "",
                    "targetValue": "Test description",
                    "commonAncestorValue": "",
                    "isMergeConflict": false,
                    "type": "modification"
                },  
                {
                    "path": "vf:Model Version Tree Folder$interestingBranch|md:v1Versioning.com.mdk1",
                    "isMergeConflict": false,
                    "isSourceDeletionAndTargetModification": false,
                    "type": "deletion"
                },
                {
                    "path": "vf:Model Version Tree Folder$interestingBranch|dm:Test Data Model",
                    "isMergeConflict": false,
                    "isSourceModificationAndTargetDeletion": false,
                    "type": "creation"
                },
            ]
        }
    }
    ```

The key point is to set the **targetValue** of every patch item to change - this value is what will be written to the target versioned folder when committing the merge.