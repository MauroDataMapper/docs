A DataElement can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "DataElement",
        "label": "element",        
        "description": "Description of the Data Element.",
        "lastUpdated": "2021-04-28T10:10:13.945Z"
        "model": "20b1fd65-a7bf-4a39-a14b-c80b0174b03e",
        "dataClass": "afb3dcda-fd7d-40b9-857c-23fb5af8cbbf",
        "dataType": {
            "id": "c85d78d3-cac8-449b-a22b-52da144b9a8f",
            "domainType": "PrimitiveType",
            "label": "integer"
        }
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this data element
- **domainType** (Type): The domain type of this catalogue object. This is always `DataElement` in this case.
- **label** (String): The human-readable identifier of this element.
- **description** (String): A long description of the data element, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **lastUpdated** (DateTime): The date/time when this DataElement was last modified
- **model** (UUID): The unique identifier of the parent data model
- **dataClass** (UUID): The unique identifier of the parent data class
- **dataType** (Object): The type definition of this data element. The object returned matches the JSON defined in [Data type](../data-type)

As well as the endpoints listed below, a DataElement is also a CatalogueItem, and so a DataElement identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Getting information

The following endpoint returns a [paginated](../pagination.md) list of all the DataElements within a particular DataClass.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements</endpoint>

This endpoint provides the detailed information about a particular DataElement under a DataClass.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements/**{id}**</endpoint>

## Create / Update / Delete

To create a new DataElement from scratch, use the following _post_ endpoint.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements</endpoint>

To edit the properties of a DataElement, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements/**{id}**</endpoint>

To delete a DataElement, use the following endpoint.

<endpoint class="delete">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements/**{id}**</endpoint>

## Copying

Instead of creating a new DataElement from scratch, it is also possible to copy an existing DataElement from another DataClass. Use the following endpoint to accomplish this. The **dataModelId** and **dataClassId** refers to the target DataClass to copy to; **otherDataModelId**, **otherDataClassId** and **dataElementId** refer to the source DataModel/Class/Element to copy from.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataElements/**{otherDataModelId}**/**{otherDataClassId}**/**{dataElementId}**</endpoint>