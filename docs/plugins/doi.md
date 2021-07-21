## Introduction

The Digital Object Identifier (DOI) plugin provides additional API endpoints that allow the integration of Mauro catalogue items to be recorded in a DOI system; this then allows unique, permanent identifiers to those catalogue items that can then be distributed across documents or articles over the web to act as links back to the Mauro content. The DOI system always ensures that a DOI name will always refer to a Mauro catalogue item as long as the DOI name is known. The plugin uses [DataCite](https://datacite.org/index.html) as the repository of Mauro DOI names; more information can be found at the DataCite website.

## Profile

### Profile summary

The plugin automatically exposes a [profile](../../glossary/profile/profile) called **Digital Object Identifiers DataCite Dataset Schema**. Depending on whether the profile is used or unused on a catalogue item, the summary of the profile can be found with one of these endpoints:

<endpoint class="get">/api/**{multiFacetAwareDomainType}**/**{id}**/profiles/used</endpoint>

<endpoint class="get">/api/**{multiFacetAwareDomainType}**/**{id}**/profiles/unused</endpoint>

=== "Response body (JSON)"
    ```json
    [
        {
            "name": "DigitalObjectIdentifiersProfileProviderService",
            "version": "1.0.0",
            "displayName": "Digital Object Identifiers DataCite Dataset Schema",
            "namespace": "uk.ac.ox.softeng.maurodatamapper.plugins.digitalobjectidentifiers.profile",
            "allowsExtraMetadataKeys": false,
            "knownMetadataKeys": [
                "identifier",
                "creator",
                "title",
                "publisher",
                "publicationYear",
                "resourceType",
                "subject",
                "contributor",
                "date",
                "language",
                "alternateIdentifier",
                "relatedIdentifier",
                "size",
                "format",
                "version",
                "rights",
                "description",
                "geolocation",
                "fundingReference",
                "relatedItem",
                "identifierType",
                "creator/fullName",
                "creator/nameType",
                "creator/givenName",
                "creator/familyName",
                "creator/nameIdentifier",
                "creator/nameIdentifierScheme",
                "creator/nameIdentifierSchemeURI",
                "creator/affiliation",
                "creator/affiliationIdentifier",
                "creator/affiliationIdentifierScheme",
                "creator/affiliationIdentifierSchemeURI",
                "titleType",
                "resourceTypeGeneral",
                "subjectScheme",
                "subjectIdentifierSchemeURI",
                "subjectIdentifierValueURI",
                "classificationCode",
                "contributorType",
                "contributor/fullName",
                "contributor/nameType",
                "contributor/givenName",
                "contributor/familyName",
                "contributor/nameIdentifier",
                "contributor/nameIdentifierScheme",
                "contributor/nameIdentifierSchemeURI",
                "contributor/affiliation",
                "contributor/affiliationIdentifier",
                "contributor/affiliationIdentifierScheme",
                "contributor/affiliationIdentifierSchemeURI",
                "dateType",
                "dateInformation",
                "alternateIdentifierType",
                "relatedIdentifier/type",
                "relatedIdentifier/relationType",
                "relatedIdentifier/metadataScheme",
                "relatedIdentifier/metadataSchemeURI",
                "relatedIdentifier/metadataSchemeType",
                "relatedIdentifier/resourceTypeGeneral",
                "rightsURI",
                "rightsIdentifier",
                "rightsIdentifierScheme",
                "rightsIdentifierSchemeURI",
                "descriptionType",
                "geoLocationPoint",
                "pointLongitude",
                "pointLatitude",
                "geoLocationBox",
                "westBoundLongitude",
                "eastBoundLongitude",
                "southBoundLongitude",
                "northBoundLongitude",
                "geoLocationPlace",
                "geoLocationPolygon",
                "polygonPoint",
                "polygonPointLongitude",
                "polygonPointLatitude",
                "funderName",
                "funderIdentifier",
                "funderIdentifierType",
                "funderIdentifierSchemeURI",
                "awardNumber",
                "awardURI",
                "awardTitle",
                "relatedItem/type",
                "relatedItem/relationType",
                "relatedItem/identifier",
                "relatedItem/identifierType",
                "relatedItem/metadataScheme",
                "relatedItem/metadataSchemeURI",
                "relatedItem/metadataSchemeType",
                "relatedItem/creator",
                "relatedItem/creator/fullName",
                "relatedItem/creator/nameType",
                "relatedItem/creator/givenName",
                "relatedItem/creator/familyName",
                "relatedItem/title",
                "relatedItem/titleType",
                "relatedItem/publicationYear",
                "relatedItem/volume",
                "relatedItem/issue",
                "relatedItem/number",
                "relatedItem/numberType",
                "relatedItem/firstPage",
                "relatedItem/lastPage",
                "relatedItem/publisher",
                "relatedItem/edition",
                "resource/contributor",
                "resource/contributor/type",
                "resource/contributor/fullName",
                "resource/contributor/nameType",
                "resource/contributor/givenName",
                "resource/contributor/familyName"
            ],
            "providerType": "Profile",
            "metadataNamespace": "org.datacite",
            "domains": [
                "VersionedFolder",
                "Folder",
                "Classifier",
                "TermRelationship",
                "TermRelationshipType",
                "Term",
                "Terminology",
                "CodeSet",
                "EnumerationValue",
                "ReferenceType",
                "PrimitiveType",
                "ModelDataType",
                "EnumerationType",
                "DataElement",
                "DataClass",
                "DataModel",
                "DataElementComponent",
                "DataClassComponent",
                "DataFlow",
                "ReferenceEnumerationValue",
                "ReferencePrimitiveType",
                "ReferenceEnumerationType",
                "ReferenceDataElement",
                "ReferenceDataModel"
            ]
        }
    ]
    ```

### Get the profile

To get the profile, use the usual profiles endpoint:

<endpoint class="get">/api/**{multiFacetAwareDomainType}**/**{id}**/profiles/**{namespace}**/**{name}**</endpoint>

For the case of the DOI profile:

* The **{namespace}** will be `uk.ac.ox.softeng.maurodatamapper.plugins.digitalobjectidentifiers.profile`.
* The **{name}** will be `DigitalObjectIdentifiersProfileProviderService`.

!!! Information
    The `GET` endpoint will always return the profile data, even if the profile has not yet been assigned to the catalogue item. In the case where it has not been assigned yet, an empty profile structure will be returned containing all the fields to prepare.

=== "Response body (JSON)"
    ```json
    {
        "sections": [
            {
                "sectionDescription": "Mandatory summary metadata fields for DOI profiles.",
                "fields": [
                    {
                        "currentValue": "",
                        "metadataPropertyName": "identifier",
                        "dataType": "STRING",
                        "fieldName": "Identifier",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "The Identifier is a unique string that identifies a resource.  For software, determine whether the identifier is for a specific version of a piece of software, (per the Force11 Software Citation Principles11), or for all versions.",
                        "minMultiplicity": 0,
                        "maxMultiplicity": 1
                    },
                    {
                        "currentValue": "",
                        "metadataPropertyName": "creator",
                        "dataType": "STRING",
                        "fieldName": "Creator",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "The main researchers involved in producing the data, or the authors of the publication, in priority order. To supply multiple creators, repeat this property.",
                        "minMultiplicity": 1,
                        "maxMultiplicity": -1
                    },
                    {
                        "currentValue": "",
                        "metadataPropertyName": "title",
                        "dataType": "TEXT",
                        "fieldName": "Title",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "A name or title by which a resource is known. May be the title of a dataset or the name of a piece of software.",
                        "minMultiplicity": 1,
                        "maxMultiplicity": -1
                    },
                    {
                        "currentValue": "",
                        "metadataPropertyName": "publisher",
                        "dataType": "STRING",
                        "fieldName": "Publisher",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role. For software, use Publisher for the code repository. If there is an entity other than a code repository, that 'holds, archives, publishes, prints, distributes, releases, issues, or produces' the code, use the property Contributor/contributorType/hostingInstitution for the code repository.",
                        "minMultiplicity": 1,
                        "maxMultiplicity": 1
                    },
                    {
                        "currentValue": "",
                        "metadataPropertyName": "publicationYear",
                        "dataType": "INT",
                        "fieldName": "Publication Year",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "The year when the data was or will be made publicly available. In the case of resources such as software or dynamic data where there may be multiple releases in one year, include the Date/dateType/dateInformation property and sub-properties to provide more information about the publication or release date details.",
                        "minMultiplicity": 1,
                        "maxMultiplicity": 1
                    },
                    {
                        "currentValue": "",
                        "metadataPropertyName": "resourceType",
                        "dataType": "TEXT",
                        "fieldName": "Resource Type",
                        "validationErrors": [],
                        "regularExpression": null,
                        "allowedValues": null,
                        "description": "A description of the resource.",
                        "minMultiplicity": 1,
                        "maxMultiplicity": 1
                    }
                ],
                "sectionName": "Mandatory DataCite DOI Fields"
            },
            {
                "sectionDescription": "Optional summary metadata fields for DOI profiles.",
                "fields": [
                    // Truncated for brevity...
                ]
                "sectionName": "Recommended DataCite DOI Fields"
            },
            {
                "sectionDescription": "Additional summary metadata fields for DOI profiles.",
                "fields": [
                    // Truncated for brevity...
                ],
                "sectionName": "Additional DataCite DOI Fields"
            }
        ],
        "id": "f5841f3f-7a63-4aa2-9c72-a64305d44dcf",
        "label": "Model Version Tree DataModel",
        "domainType": "DataModel"
    }
    ```

### Save the profile

Using the JSON structure from the `GET` endpoint above and entering values into the `sections/fields/currentValue` JSON properties, you can save the changes made to the profile, and attach the profile to the catalogue item at the same time, like so.

<endpoint class="post">/api/**{multiFacetAwareDomainType}**/**{id}**/profiles/**{namespace}**/**{name}**</endpoint>

Where:

* The **{namespace}** will be `uk.ac.ox.softeng.maurodatamapper.plugins.digitalobjectidentifiers.profile`.
* The **{name}** will be `DigitalObjectIdentifiersProfileProviderService`.

If successful, this will return the same JSON response as the `GET` endpoint above.

### Remove the profile

To remove the DOI profile from the catalogue item:

<endpoint class="delete">/api/**{multiFacetAwareDomainType}**/**{id}**/profiles/**{namespace}**/**{name}**</endpoint>

Where:

* The **{namespace}** will be `uk.ac.ox.softeng.maurodatamapper.plugins.digitalobjectidentifiers.profile`.
* The **{name}** will be `DigitalObjectIdentifiersProfileProviderService`.

## DOI Management

The profile endpoints above are standard endpoints used in Mauro. This section covers the custom endpoints added by the DOI plugin.

### Get DOI status

For any catalogue item, the current status of the DOI name on that item can be queried as follows:

<endpoint class="get">/api/**{multiFacetAwareDomainType}**/**{id}**/doi</endpoint>

=== "Response body (JSON)"
    ```json
    {
        "identifier": "10.1109/5.771073",
        "state": "final"
    }
    ```

The fields are as follows:

* **identifier** (String): The Digital Object Identifier (DOI) name assigned to this catalogue item as generated by the DOI system. If a DOI has not been generated yet, this will not be provided.
* **state** (Constant): The current DOI state of this catalogue item, which can one of:
    * **not applicable** - no DOI has been requested yet.
    * **draft** - a draft DOI has been assigned, allowing further changes to the profile.
    * **final** - a DOI has been assigned and locked, finalising this catalogue item's profile.
    * **retired** - a previous DOI has been retired and can no longer be used for cross-reference.

### Submit DOI status

Submitting the catalogue item and its DOI profile can only be done for **publicly readable** and **finalised** catalogue items. This is to ensure that:

1. Every citation has access to the catalogue item.
2. The catalogue item cannot be modified any further, keeping the citation the same for all future uses.

!!! Information
    It may be possible to not have assigned the **Digital Object Identifiers DataCite Dataset Schema** to a catalogue item before it was finalised. To solve this issue, the DOI profile has special permissions to allow it to be edited post-finalisation, so long as the DOI is not yet in the **Final** state.

    Therefore, you may use the `POST /api/**{multiFacetAwareDomainType}**/**{id}**/profiles/**{namespace}**/**{name}**` endpoint as many times as necessary to make alterations to the profile before continuing further.

To submit the catalogue item's profile to the DOI system to obtain a DOI name, use this endpoint.

<endpoint class="post">/api/**{multiFacetAwareDomainType}**/**{id}**/doi?submissionType={type}</endpoint>

This endpoint requires no request body; the profile should already have been saved before this point. The **submissionType** can be one of the following:

* **draft** - submit a draft profile to obtain the DOI name.
* **finalise** - submit a final profile to obtain the DOI name.
* **retire** - retire an existing DOI name to no longer be in active use.

The response returned will be the contents of the catalogue item the DOI was for. The plugin will also automatically populate the DOI profile `identifier` metadata key for the catalogue item.

### Remove DOI

To remove all DOI metadata:

<endpoint class="delete">/api/**{multiFacetAwareDomainType}**/**{id}**/doi</endpoint>

## DOI Resolution

The `identifier` in the DOI profile will hold the unique identifier as registered in the DOI system, for example `10.1109/5.771073`. The DOI system has a guaranteed method of locating every registered DOI name through a non-changing URL; this will actually redirect back to your client URL by providing the DOI name in the URL - in Mauro, this would be similar to `https://{domain}/#/doi/10.1109/5.771073`

To actually locate the catalogue item assigned to this DOI name, this endpoint will fetch the Mauro catalogue item to which the DOI name is mapped.

<endpoint class="get">/api/doi/**{identifier}**</endpoint>

The JSON response will contain the full catalogue item details for that DOI name. See the [REST API](../../rest-api/introduction) for the exact details returned per catalogue item domain type.