## Introduction

The Java / Groovy client library wraps the [REST API](../../rest-api/introduction.md) in Java methods to make it easy for Java developers to interact
with a Mauro instance. The library makes use of the mdm-core grails application, essentially loading a local, in-memory copy of the
[Mauro Core](../architecture.md) to take advantage of the services and controllers from Core, as well as re-using the domain model, and in-built
validation.

The REST API library can connect to a remote Mauro instance, and is typically used to perform bulk operations such as importing and exporting models,
such as when scripting a complex import. This is often the easiest way to experiment with importing before
[building a Grails Plugin](../../community/build-plugins.md). The code can also be used to connect to multiple Mauro instances, for example to copy
models from one instance to another.

## API documentation

The API is documented using GroovyDoc and the complete documentation can be [found here](./groovydoc/index.html).

## Add dependency

In order to include the Mauro client library in your Java / Groovy project, use the following dependency in Gradle or Maven:

=== "Gradle"
    ```gradle

    repositories {
        ...
        maven {url "https://jenkins.cs.ox.ac.uk/artifactory/libs-release"}
        ...
    }

    dependencies {
        ...
        compile "uk.ac.ox.softeng.maurodatamapper:mdm-api-java-restful:{version}"
    }
    ```
=== "Maven"
    ```xml
    <distributionManagement>
        <snapshotRepository>
            <id>snapshots</id>
            <name>jenkins.cs.ox.ac.uk-snapshots</name>
            <url>http://jenkins.cs.ox.ac.uk/artifactory/libs-snapshot-local</url>
        </snapshotRepository>
        ...
    </distributionManagement>
    ...
    <dependency>
        <groupId>uk.ac.ox.softeng.maurodatamapper.plugins</groupId>
        <artifactId>mdm-api-java-restful</artifactId>
        <version>{version}</version>
    </dependency>
    ```


Look on our [Release Notes](../../about/release-notes.md) page to find the latest version number

## Getting started

!!! Information 
    The examples given here are in Groovy. Conversion to equivalent Java is a fairly simple task.

The simplest way to get started is by creating a client manually - using the url of the server that the instance is hosted on, and a username /
password.

```groovy

import uk.ac.ox.softeng.maurodatamapper.api.restful.client.MauroDataMapperClient

class TestConnection {

    static void main(String[] args) {
        String baseUrl = "http://localhost:8080"
        String username = "..."
        String password = "..."
        new DataMapperClient(baseUrl, username, password).withCloseable { client ->
            // client is now connected with a session to a Mauro instance
            // Now we can do things with our client
            client.createFolder("Test Folder")
        }
    }
}
```

The `BindingMauroDataMapperClient` creates a connection to a Mauro instance, and maintains a session where necessary. The class implements the
`Closeable` interface which means that any session will be closed at the end of the `withCloseable` closure.

## Authentication and passing arguments

As in the example above, you can connect to the Mauro instance using a [username and password](../../rest-api/authentication.md). In this case, any
session cookie returned will be stored and used for future calls automatically. You can also connect using an [API Key](../../rest-api/apikeys.md) 
and this will be passed in the parameters for every call.

It's usually more convenient to pass arguments such as usernames, passwords or API keys in as parameters, rather than hard-coding them into the 
application.  We take advantage of [PicoCli](https://picocli.info) to provide options for passing these parameters to an application.

In the most basic case, consider the following application:

```groovy

import uk.ac.ox.softeng.maurodatamapper.api.restful.client.MauroDataMapperClient

class TestConnection2 extends MdmCommandLineTool<MdmConnectionOptions> {

    static void main(String[] args) {
        TestConnection2 testConnection2 = new TestConnection2(args)
        TestConnection2.doStuff()
    }
    
    void doStuff() {
        options.getMauroDataMapperClient().withCloseable { client ->
            // Do something with our client here...
        }
    }
}
```

The class extends `MdmCommandLineTool`, which provides an object of type `MdmConnectionOptions`, representing the options passed in on the command 
line.  This class contains definitions for the following options:

**-U**, **--clientBaseUrl**, **--client.baseUrl**
:   The base url of the Mauro instance to connect to - for example `http://www.example.com/mauro/`.  Any trailing `/api` will be added automatically.

**-u**, **--clientUsername**, **--client.username**
:   The username for logging into this Mauro instance.

**-p**, **--clientPassword**, **--client.password**
:   The password for logging into this Mauro instance.

**-a**, **--clientApiKey**, **--client.apiKey**
:   The API key for logging into this Mauro instance.

**-h**, **--help**
:   Displays a help message describing these options

**-v**, **--verbose**
:   Runs the application in 'verbose' mode, giving additional logging for debug purposes

**-D**, **--debug**
:   Provide advanced debug information as logs

**-P**, **--properties**
:   Provides further parameters via a properties file - for example: `--properties ./config.properties`.  See below for more details.

The final option allows these properties to be passed in a standard java properties file.  Properties should be provided using the format provided 
in the final options above - for example:

```properties
client.baseUrl=http://localhost:8080/
client.apiKey=767c6e02-4ad6-4480-8b42-a36160143a24
```
The `MdmConnectionOptions` class provides a default mechanism to create a new `BindingMauroDataMapperClient` from the provided values.
The class can be extended to provide additional, application-specific options.  To provide specific functionality for these options, you can also 
extend the `MdmCommandLineTool` class.


## Dealing with multiple connections

Occasionally, it's useful to deal with multiple connections to a single catalogue, or connections to more than one catalogue instance.  The client 
can store multiple named connections and all methods have an optional final parameter to choose which connection to use.

For example, the following code connects to two instances of Mauro, naming the connections as 'source' and 'target':

```groovy
BindingMauroDataMapperClient bindingMauroDataMapperClient = new BindingMauroDataMapperClient()
bindingMauroDataMapperClient.openConnection("source", sourceProperties)
bindingMauroDataMapperClient.openConnection("target", targetProperties)
```

Subsequent method calls can pass the name of the connection as a final argument - for example the following code copies a DataModel from the 
"source" instance of Mauro to the "target":

```groovy
DataModel dataModel = bindingMauroDataMapperClient.exportAndBindDataModelById(dataModelId, "source")

bindingMauroDataMapperClient.importDataModel(
        dataModel, folderId, dataModelName, finalised, importAsNewDocumentationVersion, "target")

```

In every method, if no connection is specified by name, the default connection (internally named "_default") is used.

## Binding vs. non-binding clients

The library provides two different clients: the first is the simpler `MauroDataMapperClient`.  This provides a number of methods for interacting
with the Mauro REST API in a more native form: dealing with responses in `Map` form.  The alternative is the more complex
`BindingMauroDataMapperClient` which extends `MauroDataMapperClient` with additional methods for binding responses into the appropriate Mauro
domain types.

For example, compare the following methods:

`Map exportDataModel(UUID id, String connectionName = defaultConnectionName)`

and

`DataModel exportAndBindDataModelById(UUID id, String connectionName = defaultConnectionName)`


The two methods access the same REST endpoint: the former returns the response JSON in map form; the latter takes that response and binds it to an 
object of class `DataModel`.  The latter is obviously easier to process, but the former provides a faster response.  

The former variant also provides an important advantage:  when a Map is bound to a Data Model within grails, it is associated with the internal, 
in-memory database and validated.  At this point, any identifiers, or 'last modified' dates associated with any component of that DataModel will 
be dropped in favour of local variants.  So, for example, if you wanted to re-use the identifiers of the DataClasses contained within that 
DataModel (for example, in order to update their descriptions individually in the remote instance), then you should use the non-binding version of 
the method.

In general, since the `BindingMauroDataMapperClient` extends the `MauroDataMapperClient` class, the binding version is all that is required.  The 
binding client has additional methods for manually binding results of calls after intermediate processing. 



