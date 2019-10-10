## Data Model object description



## List all data models


<endpoint class="get">/api/dataModels</endpoint>
<endpoint class="get">/api/admin/dataModels/deleted</endpoint>
<endpoint class="get">/api/admin/dataModels/modelSuperseded</endpoint>
<endpoint class="get">/api/admin/dataModels/documentSuperseded</endpoint>

## Get information about a particular data model

<endpoint class="get">/api/dataModels/types</endpoint>

## Create data model


## Update data model

## Delete data model
 
## Import / export a data model

<endpoint class="post">/api/dataModels/export/**{exporterNamespace}**/**{exporterName}**/**{exporterVersion}**</endpoint>
<endpoint class="post">/api/dataModels/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>



<endpoint class="get">/api/folders/**{folderId}**/dataModels</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/hierarchy</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/newVersion</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/newDocumentationVersion</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/finalise</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/readByAuthenticated</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/readByEveryone</endpoint>
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
<endpoint class="get">/api/dataModels/**{id}**</endpoint>
<endpoint class="put">/api/dataModels/**{dataModelId}**/**{type}**/**{share}**/**{shareId}**?</endpoint>
<endpoint class="delete">/api/dataModels/**{dataModelId}**/**{type}**/**{share}**/**{shareId}**</endpoint>

