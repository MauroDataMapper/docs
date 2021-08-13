The .Net client library wraps the [REST API](../../../rest-api/introduction/) in .net methods to make it easy for .Net developers to interact with a
Mauro instance. The library makes use of the .Net Core API application with Controller & Model to call API methods

The REST API library can connect to a remote Mauro instance, and is typically used to perform bulk operations such as importing and exporting models.
The code can also be used to connect to multiple Mauro instances, for example to copy models from one instance to another.

## API documentation

The API documentation is built using [DocFx](https://dotnet.github.io/docfx/) and is available [here](net/api/mdmapidotnetrestful.html):

## Adding as a dependency

In order to include the Mauro client library in your .Net project, you will need to include the following dependencies:

- CsvHelper
- Newtonsoft.Json
- System.Text.Json

A .dll file built from the code can be referenced as `mdm-api-dotnet-restful`

## API Client

MauroDataMapperClient provides constructors to login either by

1. UserId, Password, BaseUrl & Connection Name
2. Properties Object with Properties - UserName, Password & BaseUrl

If you connect to an instance using a username and password, any session cookie returned will be stored and used for future calls automatically. It's
usually more convenient to pass arguments such as usernames, passwords as command-line parameters, rather than hard-coding them into the application.

### API Client Methods

The methods of the API Client make use of the `System.Net.Http` package. This library is described in more
detail [here](https://www.nuget.org/packages/System.Net.Http/). Each accepts an object of the class `HttpRequestMessage`, and each returns an instance
of `HttpResponseMessage`

## .Net Console Application

The `mdm-api-dotnet-console` application has been built as a Windows-friendly tool for bulk CSV import.  In order to include this as part of an 
application, you need to add a reference to the `mdm-api-dotnet-restful` .dll file.

This application has its own configuration settings:

 - Folder & File location
 - Whether to create each CSV definition as a DataClass or a DataModel
   
The server address & user credentials are read from the `app.config` file. Once files are read, and their definitions uploaded to Mauro, they 
are moved to the 'Archive' folder.
