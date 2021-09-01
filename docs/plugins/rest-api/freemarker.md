## Introduction

The Freemarker plugin provides additional API endpoints that allow custom queries to be run and templates to be applied to the result. This can be
used as a lightweight way to create custom exporters or provides an easy way to allow interchange between different systems. The functionality makes
use of a popular and powerful templating engine: [Apache FreeMarker](https://freemarker.apache.org).

---

## Warning

!!! warning 
    Allowing users to execute their own code on the server is, in general, bad practice. Badly-written templates could result in the server
    becoming unresponsive or consuming additional resources. The template framework has also been carefully configured to ensure a minimal amount of 
    data is accessible, but malicious templates may be able to access more data than intended.

To mitigate this risk, the Freemarker templating plugin is an optional extra and when installed, the API endpoints are only accessible by registered
users with administrator access. It is recommended that template developers test on a local instance of Mauro in the first instance and carefully
iterate on templates. This will ensure any complex queries or loops do not accidentally cause a denial of service to the Mauro instance.

We have plans to improve the templating plugin in the future to provide greater levels of safety as well as allowing non-administrators to have access
to the functionality in a safe manner.

---

## Basic usage

The main API endpoint provided by the plugin is as follows:

<endpoint class="post">/api/**{domainType}**/**{id}**/template</endpoint>

In order to call this endpoint, the user must be authenticated as a user with an administrator role, either through a login call and a persistent
session cookie, or using an API key. The body of the call must be text corresponding to a valid Apache FreeMarker template. The `domainType` and `id`
parameters will point to a particular ‘resource’, that will be queried and have the template applied. 

Within the template, the resulting resource will be accessible through a variable with the same name as the domain type. See the examples below 
for more details. Successful return of the API call will have, as body text, the result of applying the given template to the queried resource. 

Any errors in the template will result in an error being thrown, with a `message` field indicating the nature of the error and the line number of 
the template in which the error was found.

---

## Template language reference

The [Apache FreeMarker pages](https://freemarker.apache.org) contain a general-purpose 
[introduction to the FreeMarker Template Language](https://freemarker.apache.org/docs/dgui_template_overallstructure.html) (FTL), as well as a 
[detailed reference manual](https://freemarker.apache.org/docs/ref.html) for the syntax. 

Other online tutorials are provided by [Lars Vogel](https://www.vogella.com/tutorials/FreeMarker/article.html) and some useful tricks are given in 
[this article by Baeldung](https://www.baeldung.com/freemarker-operations). 

You may also wish to visit our [Zulip community](https://maurodatamapper.zulipchat.com/) for help and advice. We would also like to publish 
reusable templates donated by the community on these pages. 

---

## Example 1: A simple web page

In this first example, a basic template will be applied to a [Data Model](../../glossary/data-model/data-model.md) in order to generate a simple HTML page for a given **Data Model**.

The API call:

<endpoint class="post">/api/dataModel/**{id}**/template</endpoint>

Is made with an appropriate API key, and the post body:

```injectedfreemarker
<html>
<body>
  <h1>
    ${dataModel.label}
  </h1>
  <p>
    ${(dataModel.description)!}
  </p>
</body>
</html>
```

Note in the template, the variable `dataModel` represents the **Data Model** object with the `id` given as the URL parameter. Note also, the use of `!`
when accessing the description o the **Data Model**. This is to guard against the case where the description is unset (null).

The body of the API call response is as follows:

```html
<html>
<body>
  <h1>
    Simple Data Model
  </h1>
  <p>
    This is the description of a simple data model
  </p>
</body>
</html>
```

Note that this example also illustrates some shortcomings of the approach for complex transformations. If the description were to be html
formatted already, for example, starting with a `<p>` tag, the resulting html may be invalid. Some simple transformations are possible within the
templating language, particularly with the use of complex macros, but the use of this plugin should be reserved for simple textual templating.  

More complex algorithms should be implemented within a custom plugin or external script, where programmatic functions and libraries are more 
easily accessible.

---

## Example 2: A CSV file of terms in a terminology

This second example uses a slightly more complex template to iterate over the terms of a terminology, printing the code and definition for each.

The API call:

<endpoint class="post">/api/terminology/**{id}**/template</endpoint>

Is made with an appropriate API key and with the following text in the body:

```injectedfreemarker
Code,Definition
<#list terminology.terms?sort_by("code") as term>
${term.code},${term.definition}
</#list>
```

The `<#list>` tag indicates a template chunk that is to be repeated for each item in the list - in this case the list of terms given by 
`terminology.term`.  The `?sort_by` annotation indicates that the set of terms should be ordered before iteration.  Within these tags, the term in 
question is given the variable name `term`.

The result is a CSV file of terms, for example:

```csv
Code,Definition
CTT00,Complex Test Term 00
CTT1,Complex Test Term 1
CTT10,Complex Test Term 10
CTT100,Complex Test Term 100
```

---

## Templating Diffs

The plugin also provides an endpoint for templating the difference between two models.  The API endpoint:

<endpoint class="post">/api/**{domainType}**/**{sourceId}**/diff/**{targetId}**/template</endpoint>

Compares two objects and allows the result to be templated.  The method provides the following variables for use within the template:

`sourceModel`
:    The model to be used as the source of the diff (left-hand side), identified by `sourceId`

`targetModel`
:    The model to be used as the target of the diff (right-hand-side), identified by `targetId`

`diff`
:    The result of the comparison between the two models, stored as a set of `diffs`

The structure of the `diff` object is still to be described in more detail, but a simple example is given below.

---

## Example 3: Listing differences

This third example gives a flavour of the templating required to examine the differences between two **Data Models**.  A more detailed example is 
needed here, but we illustrate for a very simple template, comparing two very simple (and similar) models.

Given the API call:

<endpoint class="post">/api/dataModel/**{sourceId}**/diff/**{targetId}**/template</endpoint>

With appropriate authentication and the POST body:

```injectedfreemarker
${sourceModel.label}
${targetModel.label}
<#list diff.diffs as fieldDifference> 
  ${fieldDifference.getFieldName()} :: ${fieldDifference.left} <> ${fieldDifference.right}
</#list>
```

This will print first the label of the source model, then the label of the target model.  For each basic difference between the two models, it 
will print the field name, the value of that field in the left-hand model, and the value of that field in the right-hand model.

For two very simple models this might give an output such as:

```text
Example DataModel 1
Example DataModel 2
label :: Example DataModel 1 <> Example DataModel 2
description :: My first description <> My second description
```

---