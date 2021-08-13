## What does "multi-facet" aware mean?

The "multi-facet aware" trait can be applied to any Mauro catalogue item that has at least these traits:

1. Is **metadata** aware - that is, may contain additional metadata beyond its core properties.
2. Is **annotation** aware - that is, may contain annotations or comments.
3. Is **semantic link** aware - that is, may contain semantic links to other catalogue items.
4. Is **reference file** aware - that is, may contain files or attachments for further reference material.
5. Is **rule** aware - that is, may contain rule information.

## What items are "multi-facet" aware?

The following Mauro catalogue items are multi-facet aware by the definition listed above:

1. [Classifiers](../../classification/classification)
2. Code sets
3. [Data classes](../../data-class/data-class)
4. Data class components
5. [Data elements](../../data-element/data-element)
6. Data element components
7. [Data flows](../../dataflow/dataflow)
8. [Data models](../../data-model/data-model)
9. [Data types](../../data-type/data-type)
10. [Enumeration types](../../enumeration-data-type/enumeration-data-type)
11. Enumeration values
12. [Folders](../../folder/folder)
13. Model data types
14. [Primitive types](../../primitive-data-type/primitive-data-type)
15. Reference data elements
16. Reference data models
17. [Reference data types](../../reference-data-type/reference-data-type)
18. Reference enumeration types
19. Reference enumeration values
20. Reference primitive types
21. Reference types
22. Terms
23. Term relationships
24. Term relationship types
25. Terminologies
26. [Versioned folders](../../versioned-folder/versioned-folder)

## Usage in REST API

The Mauro [REST API](../../rest-api/introduction) has many operations that are replicated across multiple catalogue item types, such as:

* Getting information on a catalogue item
* Saving data to a catalogue item
* Removing a catalogue item
* And so on...

Many of these endpoints require a **{multiFacetAwareDomainType}** parameter in their URLs. One generalised example is fetching all metadata for a catalogue item:

<endpoint class="get">/api/**{multiFacetAwareDomainType}**/**{id}**/metadata</endpoint>

Replace the **{multiFacetAwareDomainType}** parameter in these types of URL with a name listed above, remembering to:

1. Remove spaces and whitespace in the domain names.
2. Use `camelCase` for the domain name.
3. Pluralise the domain name.

Some examples would be:

* _Folder_ becomes `folders`.
* _Data Model_ becomes `dataModels`.
* _Data Class_ becomes `dataClasses`.
* _Terminology_ becomes `terminologies`.
* And so on...
