## Overview

Mauro provides a minimal set of fields that can be stored against any item in the catalogue. These are typically a [Label](../glossary/label/label.md), some other names ([Aliases](../glossary/aliases/aliases.md)) and a
description. It is expected that for any particular use of Mauro, there may be additional fields that users would want to store against a [Data Model](../glossary/data-model/data-model.md), or
component of a model. To facilitate this, Mauro allows every catalogue item to be **extensible**, by allowing any arbitrary fields to be added as the
**properties** of that object.

---

## Example 1

As a first example, consider the use of Mauro as a repository for research datasets and their discovery. For each dataset, the **Data Model**
corresponding to that dataset should have the following information stored against it:

- Responsible organisation name
- Dataset collection date
- Size of complete dataset in Megabytes
- Link to data request form

Furthermore, each [Data Element](../glossary/data-element/data-element.md) within that **Data Model** should record the following fields:

- A boolean indicating whether the field contains identifiable information
- A score denoting the completeness of the field - the number of non-null values

---

## Example 2

Consider the use of Mauro as a data asset register. Each model within Mauro represents a data asset held by the organisation. For each model (each
data asset held within the organisation), the following fields should be recorded:

- Department name
- Contact email address
- Server IP address
- Backup status

---

## Properties

Each Mauro item can hold a number of **properties**, stored as a pair of **key** and **value** fields. For example, a **Data Model** property may have the
**key**: “Responsible Organisation Name” and the **value**: “University of Oxford”. Another **Data Model** may use the same key and a different value such as
“University of Manchester”. 

Each property also has a **namespace** which is a field that can disambiguate the use of the same key for different uses. For instance, the examples above may choose to use the key **location** for their intended use case without clashing. Namespaces typically take the form of a
url (usually owned or controlled by, the use case). More information can be found
here:  [Namespace on Wikipedia](https://en.wikipedia.org/wiki/Namespace).

Mauro enforces a basic constraint upon properties where for any given catalogue item, there must be no two attached properties with the same
namespace and key. There are no constraints on values: each is stored internally as a string and can be used to store JSON or XML for more complex
values.

---

## Profiles

A profile is a group of related properties, typically sharing the same namespace. A profile allows these properties to be grouped into sections and
for each defined key may add a description, a default value and a validation constraint. The user interface is able to take known profiles and
present a cleaner interface for data entry against them. This involves hiding the namespace, grouping keys, providing the description for each field and providing
type-specific data entry controls such as date pickers. Validation can be performed for all the fields on submission.

As part of their specification, profiles can determine which types of catalogue item can use them. For example, you may have a profile which 
should only be stored against **Data Models**, or one which may be used for [Data Classes](../glossary/data-class/data-class.md) and **Data Elements** only. 

---

## Static vs Dynamic

Profiles in Mauro can be defined in one of two ways: **static** or **dynamic**. A static profile is defined as part of a plugin,
typically either stand-alone, bundled as part of an importer or exporter, or with additional functionality / REST endpoints for processing the values.
These profiles are usually defined through a JSON file, and plenty of examples can be found in the
shared [plugin repositories](https://github.com/MauroDataMapper-Plugins), such as in the SQL importers and the defined profile plugins.

Alternatively, profiles can be defined dynamically as **Data Models** within Mauro. Any model which uses the **Profile Specification Profile** is
recognised as a profile. Each **Data Class** defined at the top-level of the profile specification model represents a profile section and each **Data
Element** within those **Data Classes** defines the property keys themselves. As with any normal model, the **Profile Specification Model** can be finalised and
versioned, and it is recommended that such models are finalised before use. Find out how to create Profile Specification models in our ['Dynamic Profiles' user guide](../../user-guides/dynamic-profiles/dynamic-profiles).

Static profiles are useful when additional functionality is to be tied to the particular property values, so it is important that keys are not
changed independently. Dynamic profiles are much easier for an end-user to create, without the need to program a new Mauro Plugin. They are also
easier to re-use and extend. However, their definition must be carefully controlled to ensure the conceptual integrity of the data stored against 
them.

---