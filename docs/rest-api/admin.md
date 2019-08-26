There are a number of endpoints which are specific to administrators: understanding the configuration of the particular instance; discovering the
 avaiable plugins, etc.
 
##Currently logged in users
 
<endpoint class="get">/api/admin/activeSessions</endpoint>
 
This endpoint returns a list of all logged in users
 
<endpoint class="post">/api/admin/activeSessions</endpoint>
 
If called in 'post' mode, you can pass in user credentials, rather than basing on an existing session.

<endpoint class="delete">/api/admin/logoutAllUsers</endpoint>

This call forces the termination of all active sessions.

##Configuration

To find out more about the current instance of the catalogue: what version is running; the version of Java that's runing; the JDBC drivers
 currently available; call the following endpoint:
 
<endpoint class="get">/api/admin/status</endpoint>


###Modules

To find out which modules are installed, call the following endpoint:

<endpoint class="get">/api/admin/modules</endpoint>

The `post` version of the endpoint can be called in order to pass authentication credentials at the same time:

<endpoint class="post">/api/admin/modules</endpoint>


### Plugins

To find out which plugins are currently installed, use one of the following endpoint

<endpoint class="get">/api/admin/plugins/exporters</endpoint>
<endpoint class="get">/api/admin/plugins/emailers</endpoint>
<endpoint class="get">/api/admin/plugins/dataLoaders</endpoint>
<endpoint class="get">/api/admin/plugins/importers</endpoint>



## System properties / updates
<endpoint class="post">/api/admin/rebuildLuceneIndexes</endpoint>

This endpoint forces the rebuild of the Lucene indexes.  This is only necessary when synchronisation between database and indexes is lost; when
the search functionality is not returning correct results.  Authenticatuin credentials can be passed as part of the request body.
 
###Properties 
  
There are a number of system-wide properties that can be updated by administrators - such as the text of any emails sent, and the email address
 from which catalogue emails appear to be sent.  These can be viewed at the following endpoint:
 
<endpoint class="get">/api/admin/properties</endpoint>

... and updated at the following endpoint:

<endpoint class="post">/api/admin/editProperties</endpoint>
 
 

|   GET    |  | Action: status  |
 |   POST   | /api/admin/modules| Action: modulesWithCredentials                  |
 |   GET    | /api/admin/modules| Action: modules |
