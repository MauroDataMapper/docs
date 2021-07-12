## What does Version mean?

A **Version** of a model represents the final _state_ of that model. Changes made to a model throughout its lifetime can be tracked by their **Version numbers** to provide a history of changes made.

As an example, given a new Data Model called "Test Data Model", the **Versions** could be created as such:

1. Initial creation of "Test Data Model", then _finalised_ to be **Version 1.0.0**
2. A new draft is then created to make some alterations to the description of the model. This is then _finalised_ to be **Version 2.0.0**
3. Another new draft is then created, this time to alter the description and add Data Classes. This is then _finalised_ to be **Version 3.0.0**

...and so on.

In this way, it is possible to trace the state of each **Version** of a model from its creation to now.

**Version numbers** are _sequential_ and typically follow the same pattern as [Semantic Versioning](https://semver.org/) using **major.minor.patch**, such as **1.2.3**:

* **Major update** - represents a major change to the model, for example a major restructure. This updates the **major** number, e.g. **1.X.Y -> 2.0.0**
* **Minor update** - represents a minor, less encompasing change to the model, for example significantly updating text content but not altering the structure. This updates the **minor** number e.g. **1.0.X -> 1.1.0**
* **Patch update** - represents a very minor change to the model, for example fixing a gramatical mistake in a description. This updates the **patch** number e.g. **1.0.0 -> 1.0.1**

It is also possible to define your own custom versioning scheme.

## Why are Versions useful?

**Versions** and **Version numbers** are useful to definitively state that a model has a set contents to it and will not change; the only way to change a versioned model is to create a new version of it. This allows models to be very easily traced and makes publication of metadata very structured. **Versions** also allow readers of your models to easily tell what has changed between versions of a model.

## How are Versions created?

To create a new version of a model, please refer to the user guide [How to version and merge Data Models](../../user-guides/version-data-models/version-data-models.md).