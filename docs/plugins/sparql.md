## Introduction

The SPARQL plugin provides a compliant endpoint for executing SPARQL queries against an RDF rendering of the data. The underlying data store of Mauro
is Postgres, and this plugin uses the [D2RQ](http://d2rq.org) library for extracting the information as RDF triples. The REST API ensures that the
mapping is configured with correct access constraints so that users may only see a subset of the triples corresponding to their access privileges. In
the most basic cases, a system administrator can query across the whole data corpus in triple form; an unauthenticated user on an instance with no
publicly available models will not be able to see any triples.

!!! Warning 
    This plugin allows users to execute their own queries against the data store. A malicious user may write arbitrarily complex queries which
    could cause Mauro to slow down or become unresponsive. If you install this plugin, you may wish to ensure the Mauro instance is behind a firewall,
    and ensure that users know what they are doing!

## API Endpoints

The plugin provides two (equivalent) endpoints which accept a SPARQL query as part of the request body, and return results in a variety of formats.

<endpoint class="get">/api/sparql</endpoint>
<endpoint class="post">/api/sparql</endpoint>

The *Accept* header determines which format is returned, according to the table below:

<table>
  <thead>
    <tr>
      <th>Accept Header Value</th>
      <th>Response Format</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>application/sparql-results+xml
        <br/>xml
        <br/>application/xml
      </td>
      <td>XML</td>
    </tr>
    <tr>
      <td>text/csv
        <br/>csv
      </td>
      <td>CSV</td>
    </tr>
    <tr>
      <td>application/sparql-results+json
        <br/>json
        <br/>application/json
      </td>
      <td>JSON</td>
    </tr>
  </tbody>
</table>

The default format is for results to be returned in JSON format.

In future, it may be possible to extend this plugin to support RDF/XML and other formats.

### Response format

For the request body given in Example 1 below, the response body will have one of the following formats:  

=== "Response body (JSON)"
    ```json
    {
      "head": {
        "vars": [
          "s",
          "p",
          "o"
        ]
      },
      "results": {
        "bindings": [
          {
            "s": {
              "type": "uri",
              "value": "http://metadata-catalogue.org/datamodel/data_element/4447a37d-db1f-4524-92be-05576efe4ce5"
            },
            "p": {
              "type": "uri",
              "value": "http://metadata-catalogue.org/label"
            },
            "o": {
              "type": "literal",
              "value": "Example Data Model"
            }
          },
          ...
        ]
      }
    }
    ```
=== "Response body (XML)"
    ```xml
    <?xml version="1.0"?>
    <sparql xmlns="http://www.w3.org/2005/sparql-results#">
      <head>
        <variable name="s"/>
        <variable name="p"/>
        <variable name="o"/>
      </head>
      <results>
        <result>
          <binding name="s">
            <uri>http://metadata-catalogue.org/datamodel/data_element/4447a37d-db1f-4524-92be-05576efe4ce5</uri>
          </binding>
          <binding name="p">
            <uri>http://metadata-catalogue.org/label</uri>
          </binding>
          <binding name="o">
            <literal>Example Data Model</literal>
          </binding>
        </result>
        ...
      </results>
    </sparql>
    ```
=== "Response body (CSV)"
    ```csv
    s,p,o
    http://metadata-catalogue.org/datamodel/data_element/4447a37d-db1f-4524-92be-05576efe4ce5,http://metadata-catalogue.org/label,Example Data Model
    ...
    ```





## Example Queries

This page is not intended to provide a tutorial to writing SPARQL queries - some other tutorials are available online and linked below.  These 
examples serve as a starting point for exploring the triple space.

#### Example 1: Arbitrary triples

Select the first 20 triples from the entire graph

```sparql
SELECT ?s ?p ?o WHERE { 
    ?s ?p ?o 
} limit 20
```

#### Example 2: Restricting types

Select the labels of all data models

```sparql
PREFIX mdm: <http://metadata-catalogue.org/>

SELECT ?o WHERE {
    ?s mdm:label ?o .
    ?s a mdm:datamodel
}
```

#### Example 3: Relating entities

Find the ids of the classes which belong to a model called "Complex Test DataModel"

```sparql
PREFIX mdm: <http://metadata-catalogue.org/>

SELECT ?dcl WHERE { 
    ?dm mdm:label "Complex Test DataModel" .
    ?dm a mdm:datamodel .
    ?dm mdm:component_class ?dc .
    ?dc mdm:id ?dcl
}
```

## Links to SPARQL Tutorials

There are many good tutorials available online - this is not intended to represet a comprehensive list. But here are some some that we've found useful
in the past:

- [Apache Jena: SPARQL Tutorial](https://jena.apache.org/tutorials/sparql.html)
- [Stardog: Learn SPARQL](https://www.stardog.com/tutorials/sparql/)
- [W3C: SPARQL By Example](https://www.w3.org/2009/Talks/0615-qbe/)
