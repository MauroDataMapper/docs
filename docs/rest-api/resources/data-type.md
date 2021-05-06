A DataType can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "PrimitiveType",
        "label": "integer",        
        "description": "Represents a number.",
        "lastUpdated": "2021-04-28T10:10:13.945Z"
        "model": "20b1fd65-a7bf-4a39-a14b-c80b0174b03e",
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this data type
- **domainType** (Type): The domain type of this catalogue object. Could be `PrimitiveType` or `EnumerationType`.
- **label** (String): The human-readable identifier of this type.
- **description** (String): A long description of the data type, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **lastUpdated** (DateTime): The date/time when this DataType was last modified
- **model** (UUID): The unique identifier of the parent data model

As well as the endpoints listed below, a DataType is also a CatalogueItem, and so a DataType identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Default Data Types

When [creating DataModels](../data-model#create-data-model), a _default data type provider_ can be used to automatically define data types for a data model. To list all available data type providers:

<endpoint class="get">/api/dataModels/defaultDataTypeProviders</endpoint>

## Getting information

The following endpoint returns a [paginated](../pagination.md) list of all the DataTypes within a particular DataModel.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataTypes</endpoint>

This endpoint provides the detailed information about a particular DataType under a DataModel.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataTypes/**{id}**</endpoint>

## Create / Update / Delete

To create a new DataType from scratch, use the following _post_ endpoint.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataTypes</endpoint>

To edit the properties of a DataType, use the following endpoint, with a body similar to the JSON described at the top of this page:

<endpoint class="put">/api/dataModels/**{dataModelId}**/dataTypes/**{id}**</endpoint>

To delete a DataType, use the following endpoint.

<endpoint class="delete">/api/dataModels/**{dataModelId}**/dataTypes/**{id}**</endpoint>

## Copying

Instead of creating a new DataType from scratch, it is also possible to copy an existing DataType from another DataModel. Use the following endpoint to accomplish this. The **dataModelId** refers to the target DataModel to copy to; **otherDataModelId** and **dataTypeId** refer to the source DataModel/Type to copy from.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataTypes/**{otherDataModelId}**/**{dataTypeId}**</endpoint>
