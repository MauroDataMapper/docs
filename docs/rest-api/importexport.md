A number of plugins exist for importing and exporting Data Models, Data Flows, and Terminologies.  The endpoint for each import / export contains
 the details of the plugin to be used, which includes the namespace, the name, and the version number. 

# Data Model

## Import

The endpoint for importing one or more models is as follows:

<endpoint class="post">/api/dataModels/import/**{importerNamespace}**/**{importerName}**/**{importerVersion}**</endpoint>

Each importer defines its own set of parameters, relating to the method of import.  For example, an XML or JSON import will require a file 
upload; a SQL import will require a list of connection parameters in order to connect to a relational database.



The standard importers available with a default installation are as follows:

| Namespace | Name | Version |
| :-------- | :--- | :------ |
| ox.softeng.metadatacatalogue.plugins.excel | ExcelDataModelImporterService | 1.0.0 | 
| ox.softeng.metadatacatalogue.core.spi.xml | XmlImporterService | 2.2 | 
| ox.softeng.metadatacatalogue.core.spi.json | JsonImporterService | 1.1 | 
| ox.softeng.metadatacatalogue.plugins.database.postgres | PostgresDatabaseImporterService | 2.0.0 | 
| ox.softeng.metadatacatalogue.plugins.database.oracle | OracleDatabaseImporterService | 2.0.0 | 
| ox.softeng.metadatacatalogue.plugins.database.sqlserver | SqlServerDatabaseImporterService | 2.0.0 | 



## Export


# Data Flow

# Terminology