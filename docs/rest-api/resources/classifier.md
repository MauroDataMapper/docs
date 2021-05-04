A Classifier can be represented as follows:

=== "Response body (JSON)"
    ```json
    {
        "id": "81d00110-40e3-4ec0-b279-6004fa1b9b52",
        "domainType": "Classification",
        "label": "classifier",        
        "description": "Represents a classifier.",        
        "lastUpdated": "2021-04-28T10:10:13.945Z"        
    }
    ``` 

The fields are as follows:

- **id** (UUID): The unique identifier of this classifier
- **domainType** (Type): The domain type of this catalogue object. Will always be `Classification` in this case.
- **label** (String): The human-readable identifier of this classifier.
- **description** (String): A long description of the classifier, and any important characteristics of the data.  This field may include HTML, or 
MarkDown.
- **lastUpdated** (DateTime): The date/time when this Classifier was last modified

As well as the endpoints listed below, a Classifier is also a CatalogueItem, and so a Classifier identifier can also be used as the parameter to any 
of [those endpoints](catalogue-item.md)

## Child Classifiers

A classifier may be composed of child classifiers. Endpoints are provided to differentiate between parent and child data classifiers.

## Getting information

The following endpoints returns a [paginated](../pagination.md) list of all the Classifiers. The first requests all root classifiers in Mauro, the second requests the classifiers for a parent classifier.

<endpoint class="get">/api/classifiers</endpoint>

<endpoint class="get">/api/classifiers/**{classifierId}**/classifiers</endpoint>

These endpoints provide the detailed information about a particular Classifier; the first requests a root classifier in Mauro, the second requests a classifier from a parent classifier.

<endpoint class="get">/api/classifiers/**{id}**</endpoint>

<endpoint class="get">/api/classifiers/**{classifierId}**/classifiers/**{id}**</endpoint>

Finally, these endpoints request a list of catalogue items mapped to a classifier, and the inverse to list all classifiers mapped to a catalogue item, respectively.

<endpoint class="get">/api/classifiers/**{classifierId}**/catalogueItems</endpoint>

<endpoint class="get">/api/**{catalogueItemDomainType}**/**{catalogueItemId}**/classifiers</endpoint>

## Create / Update / Delete

To create a new Classifier from scratch, use the following _post_ endpoints, depending on whether to create one with or without a parent.

<endpoint class="post">/api/classifiers</endpoint>

<endpoint class="post">/api/classifiers/**{classifierId}**/classifiers</endpoint>

To edit the properties of a Classifier, use the following endpoints, with a body similar to the JSON described at the top of this page. Use the appropriate endpoint depending on whether to edit one with or without a parent.

<endpoint class="put">/api/classifiers/**{id}**</endpoint>

<endpoint class="put">/api/classifiers/**{classifierId}**/classifiers/**{id}**</endpoint>

To delete a Classifier, use the following endpoint, depending on whether to delete one with or without a parent. The **permanent** parameter is a boolean value that controls whether a 'hard' or 'soft' delete is used if the user is an administrator.

<endpoint class="delete">/api/classifiers/**{id}**?permanent=**{true/false}**</endpoint>

<endpoint class="delete">/api/classifiers/**{classifierId}**/classifiers/**{id}**?permanent=**{true/false}**</endpoint>

## Security

<endpoint class="delete">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="put">/api/classifiers/**{classifierId}**/readByAuthenticated</endpoint>
<endpoint class="delete">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>
<endpoint class="put">/api/classifiers/**{classifierId}**/readByEveryone</endpoint>

