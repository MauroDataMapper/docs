A number of plugins exist for importing and exporting Data Models, Data Flows, and Terminologies.  The endpoint for each import / export contains
 the details of the plugin to be used, which includes the namespace, the name, and the version number. 

# Data Model

## Import

The endpoint for importing one or more models is as follows:

<endpoint class="post">/api/dataModels/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>

Each importer defines its own set of parameters, relating to the method of import.  For example, an XML or JSON import will require a file 
upload; a SQL import will require a list of connection parameters in order to connect to a relational database.

As the import parameters may involve file attachements, standard practise is to provide upload parameters as `multipart/form-data` format, which
allows the attachment of files.     

The standard importers available with a default installation are as follows:

| Namespace | Name | Version |
| :-------- | :--- | :------ |
| ox.softeng.metadatacatalogue.plugins.excel | ExcelDataModelImporterService | 1.0.0 | 
| ox.softeng.metadatacatalogue.core.spi.xml | XmlImporterService | 2.2 | 
| ox.softeng.metadatacatalogue.core.spi.json | JsonImporterService | 1.1 | 
| ox.softeng.metadatacatalogue.plugins.database.postgres | PostgresDatabaseImporterService | 2.0.0 | 
| ox.softeng.metadatacatalogue.plugins.database.oracle | OracleDatabaseImporterService | 2.0.0 | 
| ox.softeng.metadatacatalogue.plugins.database.sqlserver | SqlServerDatabaseImporterService | 2.0.0 | 

These fall into two basic categories - simple file-based importers, or simple database-connection importers.  The parameters for each of these
 types are detailed in the sections below.

### Simple file-based importers

The simple file-based importers include the Excel, XML and JSON importers.  These take the following parameters:

| Parameter Name | Description |
| :------------- | :---------- |
| `folderId` | The UUID identifier for the folder that the new model is to be uploaded to.  This is mandatory. |
| `finalised` | A mandatory boolean value determining whether the new model is to be marked as finalised.  This determines whether the resulting model can be further edited within the interface. |
| `importAsNewDocumentationVersion` | A mandatory boolean value.  If this option is selected, then any models with the same name will be superseded.  If this option is not set, then the importer will produce an error if there are existing models with the same label. |
| `importFile` | The file containing the data to be imported - for example an XML file, JSON file, or Excel spreadsheet. |

All fields are mandatory.

### Simple database-connection importers (example)

In order to connect to a database, fields are required to build the connection string, as well as handle the resulting generated model.  Each SQL
importer is slightly different, but the SQL Server importer serves as an adequate example:

| Parameter Name | Description |
| :------------- | :---------- |
| `folderId` | The UUID identifier for the folder that the new model is to be uploaded to.  This is mandatory. |
| `finalised` | A mandatory boolean value determining whether the new model is to be marked as finalised.  This determines whether the resulting model can be further edited within the interface. |
| `importAsNewDocumentationVersion` | A mandatory boolean value.  If this option is selected, then any models with the same name will be superseded.  If this option is not set, then the importer will produce an error if there are existing models with the same label. |
| `databaseHost` | The hostname of the server that is running the database |
| `databasePort` | The port that the database is accessed through.  If none is set, then the default port for the specified database type will be used. |
| `databaseNames` | A comma-separated list of database names that are to be analysed and imported.  If multiple databases are specified, the same username and password will be used for all. |
| `databaseUsername` | The usesrname used to connect to the database |
| `databasePassword` | The password used to connect to the database |
| `domain` | The User Domain name for SQL Server.  This should be used rather than prefixing the username with `<DOMAIN>/<username>` |
| `databasesSSL` | Whether SSL should be used to connect to the database.  The default is false. |
| `useNtlmv2` | Whether to use NLTMv2 when connecting to the database. The default is false. |
| `dataModelName` | If a single database is imported, this field can be used to override its name |
| `schemaNames` | A comma-separated list of the schema names to import.  If not supplied, then all schemas other than 'sys' and 'INFORMATION_SCHEMA' will be imported | 

Other database-connecting import plugins provide a similar list of parameters, to be documented later.
 

## Export


# Data Flow

# Terminology