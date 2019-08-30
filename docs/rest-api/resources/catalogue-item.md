##Annotations

### Listing annotations

<endpoint class="get">/api/facets/**{facetOwnerId}**/annotations</endpoint>
<endpoint class="post">/api/facets/**{facetOwnerId}**/annotations</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/annotations/**{id}**</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/annotations/**{id}**</endpoint>

### Child annotations (responses)

<endpoint class="get">/api/facets/**{facetOwnerId}**/annotations/**{annotationId}**/annotations</endpoint>
<endpoint class="post">/api/facets/**{facetOwnerId}**/annotations/**{annotationId}**/annotations</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/annotations/**{annotationId}**/annotations/**{id}**</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/annotations/**{annotationId}**/annotations/**{id}**</endpoint>
 

## Searching


<endpoint class="get">/api/catalogueItems/search</endpoint>
<endpoint class="post">/api/catalogueItems/search</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/search</endpoint>
<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/search</endpoint>
<endpoint class="get">/api/classifiers/**{classifierId}**/catalogueItems</endpoint>
<endpoint class="get">/api/folders/**{folderId}**/search</endpoint>
<endpoint class="post">/api/folders/**{folderId}**/search</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/search</endpoint>
<endpoint class="post">/api/dataModels/**{dataModelId}**/search</endpoint>


## Edit History

<endpoint class="get">/api/terminologies/**{terminologyId}**/edits</endpoint>
<endpoint class="get">/api/folders/**{folderId}**/edits</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/edits</endpoint>
<endpoint class="get">/api/codeSets/**{codeSetId}**/edits</endpoint>
<endpoint class="get">/api/classifiers/**{classifierId}**/edits</endpoint>
<endpoint class="get">/api/userGroups/**{userGroupId}**/edits</endpoint>

## Metadata

<endpoint class="get">/api/metadata/namespaces/**{id}**?</endpoint>
<endpoint class="post">/api/facets/**{facetOwnerId}**/metadata</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/metadata</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/metadata/**{id}**</endpoint>
<endpoint class="put">/api/facets/**{facetOwnerId}**/metadata/**{id}**</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/metadata/**{id}**</endpoint>

## Properties

<endpoint class="get">/api/terminologies/**{terminologyId}**/permissions</endpoint>
<endpoint class="get">/api/folders/**{folderId}**/permissions</endpoint>
<endpoint class="get">/api/dataModels/**{dataModelId}**/permissions</endpoint>
<endpoint class="get">/api/codeSets/**{codeSetId}**/permissions</endpoint>
<endpoint class="get">/api/classifiers/**{classifierId}**/permissions</endpoint>

## Reference files

<endpoint class="post">/api/facets/**{facetOwnerId}**/referenceFiles</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/referenceFiles</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/referenceFiles/**{id}**</endpoint>
<endpoint class="put">/api/facets/**{facetOwnerId}**/referenceFiles/**{id}**</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/referenceFiles/**{id}**</endpoint>

## Summary Metadata

<endpoint class="post">/api/facets/**{facetOwnerId}**/summaryMetadata</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/summaryMetadata</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/summaryMetadata/**{id}**</endpoint>
<endpoint class="put">/api/facets/**{facetOwnerId}**/summaryMetadata/**{id}**</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/summaryMetadata/**{id}**</endpoint>

### Summary Metadata Reports

<endpoint class="post">/api/facets/**{facetOwnerId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports</endpoint>
<endpoint class="delete">/api/facets/**{facetOwnerId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>
<endpoint class="put">/api/facets/**{facetOwnerId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>
<endpoint class="get">/api/facets/**{facetOwnerId}**/summaryMetadata/**{summaryMetadataId}**/summaryMetadataReports/**{id}**</endpoint>


