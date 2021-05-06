There are a number of endpoints which are specific to administrators: understanding the configuration of the particular instance; discovering the
 avaiable plugins, etc.
 
 ---
 
## Currently logged in users
 
<endpoint class="get">/api/admin/activeSessions</endpoint>
 
This endpoint returns a list of all logged in users.
 
<endpoint class="post">/api/admin/activeSessions</endpoint>
 
If called in `post` mode, you can pass in user credentials, rather than basing on an existing session.

---

## Configuration

To find out more about the current instance of the catalogue: what version is running; the version of Java that's runing; the JDBC drivers
 currently available; call the following endpoint:
 
<endpoint class="get">/api/admin/status</endpoint>


### Modules

To find out which modules are installed, call the following endpoint:

<endpoint class="get">/api/admin/modules</endpoint>

The `post` version of the endpoint can be called in order to pass authentication credentials at the same time:

<endpoint class="post">/api/admin/modules</endpoint>


### Plugins

To find out which plugins are currently installed, use one of the following endpoints:

<endpoint class="get">/api/admin/plugins/exporters</endpoint>
<endpoint class="get">/api/admin/plugins/emailers</endpoint>
<endpoint class="get">/api/admin/plugins/dataLoaders</endpoint>
<endpoint class="get">/api/admin/plugins/importers</endpoint>

---

## System actions

<endpoint class="post">/api/admin/rebuildLuceneIndexes</endpoint>

This endpoint forces the rebuild of the Lucene indexes.  This is only necessary when synchronisation between database and indexes is lost; when
the search functionality is not returning correct results.  Authentication credentials can be passed as part of the request body.

---
 
## Properties 

There are a number of system-wide properties that can be updated by administrators, such as the text of any emails sent and the email address
 from which catalogue emails appear to be sent.

Properties are composed of **keys** and **values**. Keys can be any string with the following restrictions:

* Must be lowercase alpha characters
* No spaces are allowed
* May include periods ('.') and/or underscores ('_')
* Must be unique

### Getting properties
  
Properties can be viewed at the following endpoint:
 
<endpoint class="get">/api/admin/properties</endpoint>

If successful, the response body will list the available properties:

=== "Response body (JSON)"
    ```json
    {
        "count": X,
        "items": [
            {
                "id": "c7de1358-a4ce-4d72-abca-04013f7f4acc",
                "key": "test.property",
                "value": "Test value",
                "category": "Test",
                "publiclyVisible": false,
                "lastUpdatedBy": "admin@test.com",
                "createdBy": "admin@test.com",
                "lastUpdated": "2021-03-10T15:17:05.459Z"
            },
            {
                "id": "76becaa3-da04-40d5-a433-51ed203c77b4",
                "key": "test.property.public",
                "value": "Public test value",
                "category": "Test",
                "publiclyVisible": true,
                "lastUpdatedBy": "admin@test.com",
                "createdBy": "admin@test.com",
                "lastUpdated": "2021-03-10T15:17:05.558Z"
            }
        ]
    }
    ```

Notice that properties contain a `publiclyVisible` flag.  This is because properties can be created to either be public or restricted to administrators/systems 
(the default being `false`). Only an authenticated session can use the endpoint above, however an anonymous session may use this endpoint to list all publicly
available properties:

<endpoint class="get">/api/properties</endpoint>

To access a single property, this endpoint is provided:

<endpoint class="get">/api/admin/properties/**{propertyId}**</endpoint>


### Created, updating and deleting

Properties can be created as follows:

<endpoint class="post">/api/admin/properties</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "key": "test.property",
        "value": "Test value",
        "publiclyVisible": false,
        "category": "Test"
    }
    ```

If successful, the new property is returned in the response body including the new property `id`.

=== "Response body (JSON)"
    ```json
    {
        "id": "fab2b5c4-a8df-4a0a-896e-9c961dbf98aa",
        "key": "test.property",
        "value": "Test value",
        "category": "Test",
        "publiclyVisible": false,
        "lastUpdatedBy": "admin@test.com",
        "createdBy": "admin@test.com",
        "lastUpdated": "2021-03-11T17:46:47.654Z"
    }
    ```

The property can then be updated with the `put` endpoint:

<endpoint class="put">/api/admin/properties</endpoint>

=== "Request body (JSON)"
    ```json
    {
        "id": "fab2b5c4-a8df-4a0a-896e-9c961dbf98aa",
        "key": "test.property",
        "value": "Test value",
        "publiclyVisible": false,
        "category": "Test"
    }
    ```

And deleted with the `delete` endpoint:

<endpoint class="delete">/api/admin/properties/**{propertyId}**</endpoint>

---

## Data Models

The following endpoints provide paginated lists of **Data Models** (for cleaning / monitoring processes).  They list those models which have been 
deleted, superseded by a new model, and superseded by new documentation, respectively:

<endpoint class="get">/api/admin/dataModels/deleted</endpoint>
<endpoint class="get">/api/admin/dataModels/modelSuperseded</endpoint>
<endpoint class="get">/api/admin/dataModels/documentSuperseded</endpoint>

---

## Emails

Retrieve the list of emails (recipient, message, date/time) sent by the system:

<endpoint class="get">/api/admin/emails</endpoint>

---