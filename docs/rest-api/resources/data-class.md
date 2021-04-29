A DataClass can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "DataClass",
        "label": "parent",        
        "description": "Represents a parent data class.",
        "aliases": [
            "root"
        ],
        "lastUpdated": "2021-04-28T10:10:13.945Z"
        "model": "20b1fd65-a7bf-4a39-a14b-c80b0174b03e",
        "parentDataClass": "363c202b-e6d9-4098-a5bf-78194d57b70d",
        "minMultipicity": 0,
        "maxMultiplicity": -1,
        "classifiers": [
            {
                "id": "2fd9e8c7-4545-42f4-99a3-f93f14d35786",
                "label": "NIHR Health Data Finder",
                "lastUpdated": "2019-10-03T09:15:37.323Z"
            }
        ],
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this data class
- **domainType** (Type): The domain type of this catalogue object. Will always be `DataClass` in this case.
- **label** (String): The human-readable identifier of this class.
- **description** (String): A long description of the data class, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **aliases** (Set(String)): Any other names by which this data class is known
- **lastUpdated** (DateTime): The date/time when this DataClass was last modified
- **model** (UUID): The unique identifier of the owning data model
- **parentDataClass** (UUID): The unique identifier of the data class of which this is a child of. If the data class does not have a parent, this field is undefined/not provided.
- **minMultiplicity** (Number): Defines the minimum uses of this data class may be applied to a data model. See the [multipicity](#multiplicity).
- **maxMultiplicity** (Number): Defines the maximum uses of this data class may be applied to a data model. See the [multipicity](#multiplicity).
- **classifiers** (Set(Classifier)): The **id**, **label** and **lastUpdated** date of any classifiers used to tag or categorise this data class 
(see [classifiers](classifier.md))

As well as the endpoints listed below, a DataClass is also a CatalogueItem, and so a DataClass identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Child Classes

A DataClass may be composed of child classes to define more complex definitions for a DataModel. Endpoints are provided to differentiate between parent and child data classes.

## Multiplicity

Each DataClass defines its multipicity to state how many occurances of this class should be expected in a model. Multipicities are defined in the notation `x..y`, where:

* `x` represents the _minimum_ multipicity.
* `y` represents the _maximum_ multipicity.

A minimum multipicity _must_ be provided and be greater than or equal to `0`.

A maximum multiplicity _may_ be provided that is greater than or equal to `1`. To represent _unbounded_ multipicity, the `*` symbol is used - numerically, for endpoints, this is represented as the integer `-1`.

Some examples of multipicities and what they represent:

* `0..*` - an optional, unbounded data class. This may be present or not, and has not limit on how many are present.
* `1..*` - a required, unbounded data class. Similar to above but with the added constraint that at least one must be present.
* `0..1` - an optional, singular data class. Either the class is present in the model or not.
* `1..1` - a required, singular data class. This represents that the class must be present in the model.

## Getting information

The following endpoints returns a [paginated](../pagination.md) list of all the DataTypes within a particular DataModel. The first requests the data classes for a data model, the second requests the data classes for a parent data class.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses</endpoint>

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses</endpoint>

These endpoints provide the detailed information about a particular DataClass; the first requests a DataType under a particular DataModel, the second requests a DataClass from a parent DataClass.

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{id}**</endpoint>

<endpoint class="get">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses/**{id}**</endpoint>

## Create / Update / Delete

To create a new DataClass from scratch, use the following _post_ endpoints, depending on whether to create one directly under a DataModel or under a parent DataClass respectively.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses</endpoint>

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses</endpoint>

To edit the properties of a DataClass, use the following endpoints, with a body similar to the JSON described at the top of this page. Use the appropriate endpoint depending on whether to edit one directly under a DataModel or under a parent DataClass respectively.

<endpoint class="put">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses/**{id}**</endpoint>

<endpoint class="put">/api/dataModels/**{dataModelId}**/dataClasses/**{id}**</endpoint>

To delete a DataClass, use the following endpoint, depending on whether to delete one directly under a DataModel or under a parent DataClass respectively.

<endpoint class="delete">/api/dataModels/**{dataModelId}**/dataClasses/**{id}**</endpoint>

<endpoint class="delete">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses/**{id}**</endpoint>

## Copying

Instead of creating a new DataClass from scratch, it is also possible to copy an existing DataClass from another DataModel. Use the following endpoints to accomplish this, depending on whether to copy one directly under a DataModel or under a parent DataClass respectively. The **dataModelId** and **dataClassId** refers to the target DataModel or parent DataClass to copy to; **otherDataModelId** and **otherDataCLassId** refers to the source DataModel/Class to copy from.

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{otherDataModelId}**/**{otherDataClassId}**</endpoint>

<endpoint class="post">/api/dataModels/**{dataModelId}**/dataClasses/**{dataClassId}**/dataClasses/**{otherDataModelId}**/**{otherDataClassId}**</endpoint>






