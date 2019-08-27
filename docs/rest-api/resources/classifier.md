<endpoint class="POST">/api/features/**{featureComponentId}**/classifiers</endpoint>
<endpoint class="GET">/api/features/**{featureComponentId}**/classifiers</endpoint>
<endpoint class="DELETE">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>
<endpoint class="PUT">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>
<endpoint class="DELETE">/api/features/**{featureComponentId}**/classifiers/${id}</endpoint>
<endpoint class="POST">/api/classifiers</endpoint>
<endpoint class="GET">/api/classifiers</endpoint>
<endpoint class="DELETE">/api/classifiers/**{id}**</endpoint>
<endpoint class="PUT">/api/classifiers/**{id}**</endpoint>
<endpoint class="GET">/api/classifiers/**{id}**</endpoint>
<endpoint class="PUT">/api/classifiers/**{classifierId}**/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/classifiers/**{classifierId}**/${type}/${share}/${shareId}</endpoint>


<endpoint class="POST">/api/features/${featureComponentId}/classifiers</endpoint>
<endpoint class="GET">/api/features/${featureComponentId}/classifiers</endpoint>
<endpoint class="DELETE">/api/classifiers/${classifierId}/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/classifiers/${classifierId}/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/classifiers/${classifierId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/classifiers/${classifierId}/readByEveryone</endpoint>
<endpoint class="DELETE">/api/features/${featureComponentId}/classifiers/${id}</endpoint>
<endpoint class="POST">/api/classifiers</endpoint>
<endpoint class="GET">/api/classifiers</endpoint>
<endpoint class="DELETE">/api/classifiers/${id}</endpoint>
<endpoint class="PUT">/api/classifiers/${id}</endpoint>
<endpoint class="GET">/api/classifiers/${id}</endpoint>
<endpoint class="PUT">/api/classifiers/${classifierId}/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/classifiers/${classifierId}/${type}/${share}/${shareId}</endpoint>

Controller: codeSet
<endpoint class="GET">/api/folders/${folderId}/codeSets</endpoint>
<endpoint class="GET">/api/classifiers/${classifierId}/codeSets</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/newVersion</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/newDocumentationVersion</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/finalise</endpoint>
<endpoint class="DELETE">/api/codeSets/${codeSetId}/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/codeSets/${codeSetId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/codeSets/${codeSetId}</endpoint>
<endpoint class="DELETE">/api/codeSets/${codeSetId}/terms/${termId}</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/terms/${termId}</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/folder/${folderId}</endpoint>
<endpoint class="POST">/api/codeSets</endpoint>
<endpoint class="GET">/api/codeSets</endpoint>
<endpoint class="DELETE">/api/codeSets/${id}</endpoint>
<endpoint class="PUT">/api/codeSets/${id}</endpoint>
<endpoint class="GET">/api/codeSets/${id}</endpoint>
<endpoint class="PUT">/api/codeSets/${codeSetId}/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/codeSets/${codeSetId}/${type}/${share}/${shareId}</endpoint>

Controller: dataClass
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/content</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses/${id}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataClasses/${otherDataModelId}/${otherDataClassId}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/allDataClasses</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataClasses/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataClasses/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${id}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses/${otherDataModelId}/${otherDataClassId}</endpoint>

Controller: dataElement
<endpoint class="GET">/api/dataModels/${dataModelId}/dataTypes/${dataTypeId}/dataElements</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements/${id}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements/${otherDataModelId}/${otherDataClassId}/${dataElementId}</endpoint>

Controller: dataFlow
<endpoint class="POST">/api/dataModels/${dataModelId}/dataFlows/import/${importerNamespace}/${importerName}/${importerVersion}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataFlows/export/${exporterNamespace}/${exporterName}/${exporterVersion}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassFlows</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/diagramLayout</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/export/${exporterNamespace}/${exporterName}/${exporterVersion}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataFlows</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataFlows/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataFlows/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${id}</endpoint>

Controller: dataFlowComponent
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassFlows/${dataClassId}/dataFlowComponents</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents/${id}</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents/${dataFlowComponentId}/${type}/${dataElementId}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataFlowComponents/${dataFlowComponentId}/${type}/${dataElementId}</endpoint>

Controller: dataModel
<endpoint class="GET">/api/admin/dataModels/deleted</endpoint>
<endpoint class="GET">/api/admin/dataModels/modelSuperseded</endpoint>
<endpoint class="GET">/api/admin/dataModels/documentSuperseded</endpoint>
<endpoint class="GET">/api/dataModels/types</endpoint>
<endpoint class="POST">/api/dataModels/export/${exporterNamespace}/${exporterName}/${exporterVersion}</endpoint>
<endpoint class="POST">/api/dataModels/import/${importerNamespace}/${importerName}/${importerVersion}</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataClasses/clean</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataTypes/clean</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataClasses/${dataClassId}/dataElements/${dataElementId}/suggestLinks/${otherDataModelId}</endpoint>
<endpoint class="GET">/api/folders/${folderId}/dataModels</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/hierarchy</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/newVersion</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/newDocumentationVersion</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/finalise</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/dataModels/${dataModelId}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/suggestLinks/${otherDataModelId}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/diff/${otherDataModelId}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/folder/${folderId}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/export/${exporterNamespace}/${exporterName}/${exporterVersion}</endpoint>
<endpoint class="POST">/api/dataModels</endpoint>
<endpoint class="GET">/api/dataModels</endpoint>
<endpoint class="DELETE">/api/dataModels</endpoint>
<endpoint class="DELETE">/api/dataModels/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/${type}/${share}/${shareId}</endpoint>

Controller: dataType
<endpoint class="POST">/api/dataModels/${dataModelId}/dataTypes</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataTypes</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/dataTypes/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/dataTypes/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/dataTypes/${id}</endpoint>
<endpoint class="POST">/api/dataModels/${dataModelId}/dataTypes/${otherDataModelId}/${dataTypeId}</endpoint>

Controller: edit
<endpoint class="GET">/api/terminologies/${terminologyId}/edits</endpoint>
<endpoint class="GET">/api/folders/${folderId}/edits</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/edits</endpoint>
<endpoint class="GET">/api/codeSets/${codeSetId}/edits</endpoint>
<endpoint class="GET">/api/classifiers/${classifierId}/edits</endpoint>
<endpoint class="GET">/api/userGroups/${userGroupId}/edits</endpoint>

Controller: email
<endpoint class="GET">/api/admin/emails</endpoint>

Controller: enumerationValue
<endpoint class="POST">/api/dataModels/${dataModelId}/enumerationTypes/${enumerationTypeId}/enumerationValues</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/enumerationTypes/${enumerationTypeId}/enumerationValues</endpoint>
<endpoint class="DELETE">/api/dataModels/${dataModelId}/enumerationTypes/${enumerationTypeId}/enumerationValues/${id}</endpoint>
<endpoint class="PUT">/api/dataModels/${dataModelId}/enumerationTypes/${enumerationTypeId}/enumerationValues/${id}</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/enumerationTypes/${enumerationTypeId}/enumerationValues/${id}</endpoint>

Controller: folder
<endpoint class="POST">/api/folders/${folderId}/folders</endpoint>
<endpoint class="GET">/api/folders/${folderId}/folders</endpoint>
<endpoint class="DELETE">/api/folders/${folderId}/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/folders/${folderId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/readByEveryone</endpoint>
<endpoint class="DELETE">/api/folders/${folderId}/folders/${id}</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/folders/${id}</endpoint>
<endpoint class="GET">/api/folders/${folderId}/folders/${id}</endpoint>
<endpoint class="POST">/api/folders</endpoint>
<endpoint class="GET">/api/folders</endpoint>
<endpoint class="DELETE">/api/folders/${id}</endpoint>
<endpoint class="PUT">/api/folders/${id}</endpoint>
<endpoint class="GET">/api/folders/${id}</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/folders/${folderId}/${type}/${share}/${shareId}</endpoint>

Controller: global
<endpoint class="GET">/api/public/defaultDataTypeProviders</endpoint>

Controller: importer
<endpoint class="GET">/api/importer/parameters/${ns}?/${name}?/${version}?</endpoint>

Controller: metadata
<endpoint class="GET">/api/metadata/namespaces/${id}?</endpoint>
<endpoint class="POST">/api/facets/${facetOwnerId}/metadata</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/metadata</endpoint>
<endpoint class="DELETE">/api/facets/${facetOwnerId}/metadata/${id}</endpoint>
<endpoint class="PUT">/api/facets/${facetOwnerId}/metadata/${id}</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/metadata/${id}</endpoint>

Controller: permissions
<endpoint class="GET">/api/terminologies/${terminologyId}/permissions</endpoint>
<endpoint class="GET">/api/folders/${folderId}/permissions</endpoint>
<endpoint class="GET">/api/dataModels/${dataModelId}/permissions</endpoint>
<endpoint class="GET">/api/codeSets/${codeSetId}/permissions</endpoint>
<endpoint class="GET">/api/classifiers/${classifierId}/permissions</endpoint>

Controller: plugin
<endpoint class="GET">/api/public/plugins/dataFlowImporters</endpoint>
<endpoint class="GET">/api/public/plugins/dataFlowExporters</endpoint>
<endpoint class="GET">/api/public/plugins/dataModelImporters</endpoint>
<endpoint class="GET">/api/public/plugins/dataModelExporters</endpoint>

Controller: referenceFile
<endpoint class="POST">/api/facets/${facetOwnerId}/referenceFiles</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/referenceFiles</endpoint>
<endpoint class="DELETE">/api/facets/${facetOwnerId}/referenceFiles/${id}</endpoint>
<endpoint class="PUT">/api/facets/${facetOwnerId}/referenceFiles/${id}</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/referenceFiles/${id}</endpoint>

Controller: semanticLink
<endpoint class="POST">/api/terminologies/${terminologyId}/terms/${termId}/semanticLinks</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${termId}/semanticLinks</endpoint>
<endpoint class="DELETE">/api/terminologies/${terminologyId}/terms/${termId}/semanticLinks/${id}</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/terms/${termId}/semanticLinks/${id}</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${termId}/semanticLinks/${id}</endpoint>
<endpoint class="POST">/api/catalogueItems/${catalogueItemId}/semanticLinks</endpoint>
<endpoint class="GET">/api/catalogueItems/${catalogueItemId}/semanticLinks</endpoint>
<endpoint class="DELETE">/api/catalogueItems/${catalogueItemId}/semanticLinks/${id}</endpoint>
<endpoint class="PUT">/api/catalogueItems/${catalogueItemId}/semanticLinks/${id}</endpoint>
<endpoint class="GET">/api/catalogueItems/${catalogueItemId}/semanticLinks/${id}</endpoint>

Controller: summaryMetadata
<endpoint class="POST">/api/facets/${facetOwnerId}/summaryMetadata</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/summaryMetadata</endpoint>
<endpoint class="DELETE">/api/facets/${facetOwnerId}/summaryMetadata/${id}</endpoint>
<endpoint class="PUT">/api/facets/${facetOwnerId}/summaryMetadata/${id}</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/summaryMetadata/${id}</endpoint>

Controller: summaryMetadataReport
<endpoint class="POST">/api/facets/${facetOwnerId}/summaryMetadata/${summaryMetadataId}/summaryMetadataReports</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/summaryMetadata/${summaryMetadataId}/summaryMetadataReports</endpoint>
<endpoint class="DELETE">/api/facets/${facetOwnerId}/summaryMetadata/${summaryMetadataId}/summaryMetadataReports/${id}</endpoint>
<endpoint class="PUT">/api/facets/${facetOwnerId}/summaryMetadata/${summaryMetadataId}/summaryMetadataReports/${id}</endpoint>
<endpoint class="GET">/api/facets/${facetOwnerId}/summaryMetadata/${summaryMetadataId}/summaryMetadataReports/${id}</endpoint>

Controller: term
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/search/${search}?</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${termId}/tree</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms</endpoint>
<endpoint class="GET">/api/codeSets/${codeSetId}/terms</endpoint>
<endpoint class="GET">/api/classifiers/${classifierId}/terms</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${id}</endpoint>

Controller: termRelationship
<endpoint class="GET">/api/terminologies/${terminologyId}/termRelationshipTypes/${termRelationshipTypeId}/termRelationships</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${termId}/termRelationships</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/termRelationshipTypes/${termRelationshipTypeId}/termRelationships/${id}</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/terms/${termId}/termRelationships/${id}</endpoint>

Controller: termRelationshipType
<endpoint class="GET">/api/terminologies/${terminologyId}/termRelationshipTypes</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/termRelationshipTypes/${id}</endpoint>

Controller: terminology
<endpoint class="GET">/api/admin/terminologies/deleted</endpoint>
<endpoint class="GET">/api/admin/terminologies/modelSuperseded</endpoint>
<endpoint class="GET">/api/admin/terminologies/documentSuperseded</endpoint>
<endpoint class="POST">/api/terminologies/import/${type}</endpoint>
<endpoint class="GET">/api/classifiers/${classifierId}/terminologies</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/tree</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/newVersion</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/newDocumentationVersion</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/finalise</endpoint>
<endpoint class="DELETE">/api/terminologies/${terminologyId}/readByAuthenticated</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/readByAuthenticated</endpoint>
<endpoint class="DELETE">/api/terminologies/${terminologyId}/readByEveryone</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/readByEveryone</endpoint>
<endpoint class="GET">/api/terminologies/${terminologyId}/export/${type}</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/folder/${folderId}</endpoint>
<endpoint class="PUT">/api/folders/${folderId}/terminologies/${terminologyId}</endpoint>
<endpoint class="POST">/api/terminologies</endpoint>
<endpoint class="GET">/api/terminologies</endpoint>
<endpoint class="DELETE">/api/terminologies/${id}</endpoint>
<endpoint class="PUT">/api/terminologies/${id}</endpoint>
<endpoint class="GET">/api/terminologies/${id}</endpoint>
<endpoint class="PUT">/api/terminologies/${terminologyId}/${type}/${share}/${shareId}?</endpoint>
<endpoint class="DELETE">/api/terminologies/${terminologyId}/${type}/${share}/${shareId}</endpoint>

Controller: treeItem
<endpoint class="GET">/api/tree/search/${search}</endpoint>
<endpoint class="GET">/api/tree/${id}?</endpoint>

Controller: userGroup
<endpoint class="GET">/api/userGroups/${userGroupId}/catalogueUsers</endpoint>
<endpoint class="DELETE">/api/userGroups/${userGroupId}/catalogueUsers/${catalogueUserId}</endpoint>
<endpoint class="PUT">/api/userGroups/${userGroupId}/catalogueUsers/${catalogueUserId}</endpoint>
<endpoint class="POST">/api/userGroups</endpoint>
<endpoint class="GET">/api/userGroups</endpoint>
<endpoint class="DELETE">/api/userGroups/${id}</endpoint>
<endpoint class="PUT">/api/userGroups/${id}</endpoint>
<endpoint class="GET">/api/userGroups/${id}</endpoint>



