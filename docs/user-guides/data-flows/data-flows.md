Mauro has the capacity to record data flows, which data goes to where. These used to be in the UI, but are currently only accessible via the API.
[Data Flows in the glossary](../../glossary/dataflow/dataflow.md)

The domain setup is a dataFlow "has many" dataClassComponents which "has Many" dataElementComponents. A target of a dataFlow can have many sources. A source of a dataFlow can have many targets. 

Data Flows can only be created between models of the 'Asset' type.
```
{
    "total": 1,
    "errors": [
        {
            "message": "Property [target] of DataFlow cannot by model type [Data Standard]"
        }
    ]
}
```
In order to express relation between Assets and Standards, use Semantic Links - an Asset `refines` a Standard.

--------------------------------
In order to create a flow, you need to use the endpoints of:
```
 |   POST   | /api/dataModels/${targetDataModelId}/dataFlows         | Action: save
 |   GET    | /api/dataModels/${targetDataModelId}/dataFlows         | Action: index
 |  DELETE  | /api/dataModels/${targetDataModelId}/dataFlows/${id}   | Action: delete
 |   PUT    | /api/dataModels/${targetDataModelId}/dataFlows/${id}   | Action: update
 |   GET    | /api/dataModels/${targetDataModelId}/dataFlows/${id}   | Action: show
```
required JSON for a POST:
```
{
  "label" : "Functional Test DataFlow",
  "source": "sourceDataModelId"
}
```

You can 'reverse' these endpoints and use `${sourceDataModelId}` in the endpoint URL, with `?type=source` in the url. Then target ID in the JSON.

**_CAUTION:_** It is entirely possible to create dataFlows with the same label name as other dataFlows. This may cause significant confusion, and should be avoided.

what you'll get from a "show":
```
{
  "id": "${json-unit.matches:id}",
  "domainType": "DataFlow",
  "label": "Functional Test DataFlow",
  "model": "${json-unit.matches:id}",
  "breadcrumbs": [
    {
      "id": "${json-unit.matches:id}",
      "label": "TargetFlowDataModel",
      "domainType": "DataModel",
      "finalised": false
    }
  ],
  "availableActions": [
    "delete",
    "show",
    "update"
  ],
  "lastUpdated": "${json-unit.matches:offsetDateTime}",
  "definition": null,
  "source": {
    "id": "${json-unit.matches:id}",
    "domainType": "DataModel",
    "label": "SourceFlowDataModel",
    "type": "Data Asset",
    "branchName": "main",
    "documentationVersion": "1.0.0"
  },
  "target": {
    "id": "${json-unit.matches:id}",
    "domainType": "DataModel",
    "label": "TargetFlowDataModel",
    "type": "Data Asset",
    "branchName": "main",
    "documentationVersion": "1.0.0"
  },
  "diagramLayout": null
}
```
----------------------------------------------------------

Ollie Freeman:
The index/list endpoint is quite powerful - if you provide the dataModelId it will find the entire chain of DFs that DM is on.
You need to use the param `type=source` or `type=target` to get a single direction.

This is all under the condition you can read all of the chain, if you cannot read a DM then it will not show a flow between that model and another. It will stop once it hits an unreadable model.

One of the things we also want to add is an inference .... so infer the flow DM.1->DM.3 ... that way if you can read 1 and 3 then you can see the flow but you cant see DM2

-------------------------------------------------------------
Once a dataFlow is created between dataModels, the components of which classes and elements relate to each other have to be created. These use the endpoints below. Note with these endpoints that Mauro does NOT implicitly create the elements in the pathway if they do not exist. You need to create the dataFlow, then the dataClassComponent, then any dataElementComponents that are part of it.

**_CAUTION:_** It is entirely possible to create cyclical dataFlows, and this will have detrimental effects on any automation. These are not currently detected by the system, so there is trust in the user not to create them, or to remove any that are found.

**_CAUTION:_** It is entirely possible to create dataClassComponents or dataElementComponents with the same label name as others. This may cause significant confusion, and should be avoided.

When using these endpoints:
- the dataModelId is the Target dataModelId.
- `${type}` can be one of `source`, `target`

```
Controller: dataClassComponent
 |   POST   | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents           | Action: save
 |   GET    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents           | Action: index
 |  DELETE  | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${id}     | Action: delete
 |   PUT    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${id}     | Action: update
 |   GET    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${id}     | Action: show
 |  DELETE  | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/${type}/${dataClassId}    | Action: alterDataClasses
 |   PUT    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/${type}/${dataClassId}    | Action: alterDataClasses
```
```
{
  "label"            : "Functional Test DataClassComponent",
  "sourceDataClasses": "[sourceDataClassId]",
  "targetDataClasses": "[targetDataClassId]"
}
```
```
Controller: dataElementComponent
 |   POST   | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents                                                         | Action: save
 |   GET    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents                                                         | Action: index
 |  DELETE  | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents/${id}                                                   | Action: delete
 |   PUT    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents/${id}                                                   | Action: update
 |   GET    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents/${id}                                                   | Action: show
 |  DELETE  | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents/${dataElementComponentId}/${type}/${dataElementId}      | Action: alterDataElements
 |   PUT    | /api/dataModels/${dataModelId}/dataFlows/${dataFlowId}/dataClassComponents/${dataClassComponentId}/dataElementComponents/${dataElementComponentId}/${type}/${dataElementId}      | Action: alterDataElements
```
```
{
  "label"            : "Functional Test DataElementComponent",
  "sourceDataElements": "[sourceDataElementId]",
  "targetDataElements": "[targetDataElementId]"
}
```
-------------------------------------------------

dataFlows are currently independent of versions of the dataModels. This means that if you have a dataFlow on a versioned model, and create a new version, the flow will not be copied/ created onto the new version of the model. Functionality to handle this is envisaged for release in 2022.
