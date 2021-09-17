## Introduction

The Digital Object Identifier (DOI) plugin provides additional API endpoints that allow the integration of any Mauro [multi-facet aware](../../../glossary/multi-facet-aware/multi-facet-aware) catalogue item to be recorded in a DOI system; this then allows unique, permanent identifiers to those catalogue items that can then be distributed across documents or articles over the web to act as links back to the Mauro content. The DOI system always ensures that a DOI name will always refer to a Mauro catalogue item as long as the DOI name is known. The plugin uses [DataCite](https://datacite.org/index.html) as the repository of Mauro DOI names; more information can be found at the DataCite website.

In order to use Digital Object Identifiers, the Mauro instance must:

1. Have the **Mauro Digital Object Identifier plugin** installed.
2. Set up and configure DataCite to acts as the DOI system.

The full details of this set up can be viewed in the user guide [Using Digital Object Identifiers](../../user-guides/digital-object-identifiers/digital-object-identifiers).

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
            "version": "1.1.0",
            "displayName": "Digital Object Identifiers DataCite Dataset Schema",
            "namespace": "uk.ac.ox.softeng.maurodatamapper.plugins.digitalobjectidentifiers.profile",
            "allowsExtraMetadataKeys": false,
            "knownMetadataKeys": [
                "identifier",
                "prefix",
                "suffix",
                "status",
                "state",
                "titles/mainTitle",
                "descriptions/mainDescription",
                "version",
                "creators/creator/creatorName",
                "creators/creator/creatorNameType",
                "creators/creator/givenName",
                "creators/creator/familyName",
                "creators/creator/nameIdentifier",
                "creators/creator/affiliation",
                "publisher",
                "publicationYear",
                "resourceType",
                "titles/title",
                "titles/titleType",
                "descriptions/description",
                "descriptions/descriptionType",
                "contributors/contributor/contributorName",
                "contributors/contributor/contributorNameType",
                "contributors/contributor/contributorType",
                "contributors/contributor/givenName",
                "contributors/contributor/familyName",
                "contributors/contributor/nameIdentifier",
                "contributors/contributor/affiliation",
                "language"
            ],
            "providerType": "Profile",
            "metadataNamespace": "org.datacite",
            "domains": [
                "VersionedFolder",
                "Folder",
                "Classifier",
                "ReferenceType",
                "PrimitiveType",
                "ModelDataType",
                "EnumerationType",
                "EnumerationValue",
                "DataElement",
                "DataClass",
                "DataModel",
                "DataFlow",
                "DataElementComponent",
                "DataClassComponent",
                "Terminology",
                "TermRelationshipType",
                "TermRelationship",
                "Term",
                "CodeSet",
                "ReferenceDataModel",
                "ReferenceDataElement",
                "ReferencePrimitiveType",
                "ReferenceEnumerationType",
                "ReferenceEnumerationValue"
            ],
            "editableAfterFinalisation": true
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
                "name": "Predefined/Supplied Fields",
                "description": "Fixed fields which cannot be changed.",
                "fields": [
                    {
                        "fieldName": "Identifier",
                        "metadataPropertyName": "identifier",
                        "description": "A persistent identifier that identifies a resource. This will be filled in by the API upon submission",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": true,
                        "currentValue": "10.80079/ynk3-sz81"
                    },
                    {
                        "fieldName": "Prefix",
                        "metadataPropertyName": "prefix",
                        "description": "DOI prefix. The first part of the identifier",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": true,
                        "currentValue": "10.80079"
                    },
                    {
                        "fieldName": "Suffix",
                        "metadataPropertyName": "suffix",
                        "description": "DOI suffix. The last part of the identifier",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": true,
                        "currentValue": "ynk3-sz81"
                    },
                    {
                        "fieldName": "Status",
                        "metadataPropertyName": "status",
                        "description": "Status of DOI: draft, final, retired, not submitted.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": true,
                        "currentValue": "retired"
                    },
                    {
                        "fieldName": "State",
                        "metadataPropertyName": "state",
                        "description": "State of DOI inside DataCite: draft, findable, registered (Registered indicates a retired DOI).",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": true,
                        "currentValue": "registered"
                    },
                    {
                        "fieldName": "Main Title",
                        "metadataPropertyName": "titles/mainTitle",
                        "description": "The main title by which the resource is known, derived from the label field of the resource.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "text",
                        "derived": true,
                        "derivedFrom": "label",
                        "uneditable": true,
                        "currentValue": "DOI Test Model 5"
                    },
                    {
                        "fieldName": "Main Description",
                        "metadataPropertyName": "descriptions/mainDescription",
                        "description": "The main description for the resource, derived from the description field of the resource.",
                        "maxMultiplicity": -1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "text",
                        "derived": true,
                        "derivedFrom": "description",
                        "uneditable": true,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Version",
                        "metadataPropertyName": "version",
                        "description": "Version number of the resource. If the primary resource has changed the version number increases. Register a new identifier for a major version change. Individual stewards need to determine which are major vs. minor versions. May be used in conjunction with properties 11 and 12 (AlternateIdentifier and RelatedIdentifier) to indicate various information updates. May be used in conjunction with property 17 (Description) to indicate the nature and file/record range of version.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": true,
                        "derivedFrom": "modelVersion",
                        "uneditable": true,
                        "currentValue": "1.0.0"
                    }
                ]
            },
            {
                "name": "Primary Creator",
                "description": "Resource Creator. This section will be capable of accepting multiples in the future, however at the moment it only handles a single entry.",
                "fields": [
                    {
                        "fieldName": "Name",
                        "metadataPropertyName": "creators/creator/creatorName",
                        "description": "The main researchers involved working on the data, or the authors of the publication in priority order. May be a corporate/institutional or personal name.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": "Peter Monks"
                    },
                    {
                        "fieldName": "Name Type",
                        "metadataPropertyName": "creators/creator/creatorNameType",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": [
                            "Organizational",
                            "Personal"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": "Personal"
                    },
                    {
                        "fieldName": "Given Name",
                        "metadataPropertyName": "creators/creator/givenName",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Family Name",
                        "metadataPropertyName": "creators/creator/familyName",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Identifier",
                        "metadataPropertyName": "creators/creator/nameIdentifier",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Affiliation",
                        "metadataPropertyName": "creators/creator/affiliation",
                        "description": "Affiliation of creator, company or institution they represent",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    }
                ]
            },
            {
                "name": "Additional Mandatory Fields",
                "description": null,
                "fields": [
                    {
                        "fieldName": "Publisher",
                        "metadataPropertyName": "publisher",
                        "description": "The name of the entity that holds, archives, publishes prints, distributes, releases, issues, or produces the resource. This property will be used to formulate the citation, so consider the prominence of the role. For software, use Publisher for the code repository. If there is an entity other than a code repository, that 'holds, archives, publishes, prints, distributes, releases, issues, or produces' the code, use the property Contributor/contributorType/hostingInstitution for the code repository.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": "OCC"
                    },
                    {
                        "fieldName": "Publication Year",
                        "metadataPropertyName": "publicationYear",
                        "description": "The year when the data was or will be made publicly available. If an embargo period has been in effect, use the date when the embargo period ends.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": null,
                        "regularExpression": "\\d{4}",
                        "dataType": "int",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": "2021"
                    },
                    {
                        "fieldName": "Resource Type",
                        "metadataPropertyName": "resourceType",
                        "description": "The type of a resource",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 1,
                        "allowedValues": [
                            "Audiovisual",
                            "Book",
                            "BookChapter",
                            "Collection",
                            "ComputationalNotebook",
                            "ConferencePaper",
                            "ConferenceProceeding",
                            "DataPaper",
                            "Dataset",
                            "Dissertation",
                            "Event",
                            "Image",
                            "InteractiveResource",
                            "Journal",
                            "JournalArticle",
                            "Model",
                            "OutputManagementPlan",
                            "PeerReview",
                            "PhysicalObject",
                            "Preprint",
                            "Report",
                            "Service",
                            "Software",
                            "Sound",
                            "Standard",
                            "Text",
                            "Workflow",
                            "Other"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": "Collection"
                    }
                ]
            },
            {
                "name": "Additional Optional Title Section",
                "description": "This section will be capable of accepting multiples in the future, however at the moment it only handles a single entry.",
                "fields": [
                    {
                        "fieldName": "Title",
                        "metadataPropertyName": "titles/title",
                        "description": "A name or title by which a resource is known.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Title Type",
                        "metadataPropertyName": "titles/titleType",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": [
                            "AlternativeTitle",
                            "Subtitle",
                            "TranslatedTitle",
                            "Other"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    }
                ]
            },
            {
                "name": "Additional Optional Description Section",
                "description": "This section will be capable of accepting multiples in the future, however at the moment it only handles a single entry.",
                "fields": [
                    {
                        "fieldName": "Description",
                        "metadataPropertyName": "descriptions/description",
                        "description": "All additional information that does not fit in any of the other categories. May be used for technical information.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "text",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Description Type",
                        "metadataPropertyName": "descriptions/descriptionType",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": [
                            "Abstract",
                            "Methods",
                            "SeriesInformation",
                            "TableOfContents",
                            "TechnicalInfo",
                            "Other"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    }
                ]
            },
            {
                "name": "Primary Contributor",
                "description": "Resource Contributor. This section will be capable of accepting multiples in the future, however at the moment it only handles a single entry.",
                "fields": [
                    {
                        "fieldName": "Name",
                        "metadataPropertyName": "contributors/contributor/contributorName",
                        "description": "The institution or person responsible for collecting, creating, or otherwise contributing to the development of the dataset.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Name Type",
                        "metadataPropertyName": "contributors/contributor/contributorNameType",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": [
                            "Organizational",
                            "Personal"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Contributor Type",
                        "metadataPropertyName": "contributors/contributor/contributorType",
                        "description": "Mandatory if the contributor name is provided.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": [
                            "ContactPerson",
                            "DataCollector",
                            "DataCurator",
                            "DataManager",
                            "Distributor",
                            "Editor",
                            "HostingInstitution",
                            "Other",
                            "Producer",
                            "ProjectLeader",
                            "ProjectManager",
                            "ProjectMember",
                            "RegistrationAgency",
                            "RegistrationAuthority",
                            "RelatedPerson",
                            "ResearchGroup",
                            "RightsHolder",
                            "Researcher",
                            "Sponsor",
                            "Supervisor",
                            "WorkPackageLeader"
                        ],
                        "regularExpression": null,
                        "dataType": "enumeration",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Given Name",
                        "metadataPropertyName": "contributors/contributor/givenName",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Family Name",
                        "metadataPropertyName": "contributors/contributor/familyName",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Identifier",
                        "metadataPropertyName": "contributors/contributor/nameIdentifier",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    },
                    {
                        "fieldName": "Affiliation",
                        "metadataPropertyName": "contributors/contributor/affiliation",
                        "description": null,
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    }
                ]
            },
            {
                "name": "Additional Optional Fields",
                "description": "Optional metadata fields for DOI profiles.",
                "fields": [
                    {
                        "fieldName": "Language",
                        "metadataPropertyName": "language",
                        "description": "Primary language of the resource. Allowed values are taken from  IETF BCP 47, ISO 639-1 language codes. For English, use 'en'.",
                        "maxMultiplicity": 1,
                        "minMultiplicity": 0,
                        "allowedValues": null,
                        "regularExpression": null,
                        "dataType": "string",
                        "derived": false,
                        "derivedFrom": null,
                        "uneditable": false,
                        "currentValue": ""
                    }
                ]
            }
        ],
        "id": "36e74acc-a862-43d0-8e2b-e54422c4239f",
        "label": "DOI Test Model 5",
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

If a status exists, a `200 OK` response will be returned with this response body:

=== "Response body (JSON)"
    ```json
    {
        "identifier": "10.1109/5.771073",
        "status": "final"
    }
    ```

The fields are as follows:

* **identifier** (String): The Digital Object Identifier (DOI) name assigned to this catalogue item as generated by the DOI system. If a DOI has not been generated yet, this will not be provided.
* **state** (Constant): The current DOI state of this catalogue item, which can one of:
    * **not submitted** - no DOI has been requested yet.
    * **draft** - a draft DOI has been assigned, allowing further changes to the profile.
    * **final** - a DOI has been assigned and locked, finalising this catalogue item's profile.
    * **retired** - a previous DOI has been retired and can no longer be used for cross-reference.

### Submit DOI status

Submitting the catalogue item and its DOI profile can only be done for **publicly readable** and **finalised** catalogue items. This is to ensure that:

1. Every citation has access to the catalogue item.
2. The catalogue item cannot be modified any further, keeping the citation the same for all future uses.

!!! Information
    It may be possible to not have assigned the **Digital Object Identifiers DataCite Dataset Schema** to a catalogue item before it was finalised. To solve this issue, the DOI profile has special permissions to allow it to be edited post-finalisation, so long as the DOI is not yet in the **Final** state.

    Therefore, you may use the `POST /api/{multiFacetAwareDomainType}/{id}/profiles/{namespace}/{name}` endpoint as many times as necessary to make alterations to the profile before continuing further.

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