As well as providing Mauro endpoints for importing from remote databases, the database import plugins can be used as standalone command-line interface (CLI) tools to import to
a remote Mauro instance from a database.

Each database-specific import plugin provides a command line tool for Unix-like and Windows platforms that can import from a remote database. The command line parameters are
the same for the different tools, and they each read a configuration file with some common parameters, and some database-specific parameters.

## Command-line usage

The provided command line tools are:

| Database plugin | CLI tool name |
| :-------------- | :------------ |
| mdm-plugin-database-mysql | `mysql-remote-database-importer` |
| mdm-plugin-database-oracle | `oracle-remote-database-importer` |
| mdm-plugin-database-postgresql | `postgres-remote-database-importer` |
| mdm-plugin-database-sqlserver | `sqlserver-remote-database-importer` |

Usage, replacing `remote-database-importer` with a CLI tool named above:

> ***remote-database-importer*** -c *&lt;FILE&gt;* -u *&lt;USERNAME&gt;* -p *&lt;PASSWORD&gt;* -w *&lt;DATABASE_PASSWORD&gt;*
>
> Import database to Mauro Data Mapper  
> Connect to a database, import to a DataModel and push to the Mauro server
>
>
> `-c`, `--config` *&lt;FILE&gt;*
> : Config file defining the import configuration (required)
>
> `-h`, `--help`
>
> `-p`, `--password` *&lt;PASSWORD&gt;*
> : Password for Mauro Data Mapper instance (required)
>
> `-u`, `--username` *&lt;USERNAME&gt;*
> : Username for Mauro Data Mapper instance (required)
>
> `-v`, `--version`
>
>  `-w`, `--databasePassword` *&lt;DATABASE_PASSWORD&gt;*
> : Password for the database to import (required)

### Configuration parameters

The configuration file (params `-c`, `--config`) uses the Java properties format (an example is [below](#example-usage)) and all the importers take the following parameters in
this file:

| Parameter | Usage |
| :-------- | :---- |
| `import.database.name` | Database name to import |
| `import.database.names` | Database names to import (comma separated list, if importing multiple databases) |
| `import.database.host` | Database hostname |
| `import.database.username` | Database username |
| `import.database.ssl` | Enable SSL for database connection (`true` or `false`) |
| `import.database.port` | Database port (if not using default) |
| `export.server.url` | URL of remote Mauro instance to import to |
| `export.folder.path` | Folder path to export to |
| `export.dataModel.name` | Data model name to export (optional) |
| `export.dataModel.finalised` | Export data model as finalised (`true` or `false`, default is `true`) |

Some of the importers also take database-specific parameters:

#### `oracle-remote-database-importer` configuration parameters

| Parameter | Usage |
| :-------- | :---- |
| import.database.owner | Database owner to import from |

#### `postgres-remote-database-importer` configuration parameters

| Parameter | Usage |
| :-------- | :---- |
| import.database.schemas | Database schemas to import from (comma separated list, optional) |

#### `sqlserver-remote-database-importer` configuration parameters

| Parameter | Usage |
| :-------- | :---- |
| import.database.schemas | Database schemas to import from (comma separated list, optional) |

### Example usage

An example of invoking `postgres-remote-database-importer`:

```shell
./postgres-remote-database-importer -c config.properties -u admin@maurodatamapper.com -p password -w MauroDataMapper1234
```

Where `config.properties` contains:

```properties
import.database.name=metadata_simple
import.database.host=localhost
import.database.username=maurodatamapper
import.database.ssl=false
export.server.url=http://localhost:8080
export.folder.path=8b5523d9-dfd2-4185-a49c-51b9e2f4c515
export.dataModel.name=Model from Postgres DB
```

A DataModel named 'Model from Postgres DB' is imported from the database 'metadata_simple' on the Postgres database at `localhost` (on default port 5432), to the Mauro
instance at `http://localhost:8080`, and is placed in the top level folder with ID `8b5523d9-dfd2-4185-a49c-51b9e2f4c515`.

### Building command-line tools

To build a command line tool from one of the database importer plugin projects, run `gradle distTar` to build a Unix distribution or `gradle distZip` to build a Windows
distribution. The outputs are found in the `build/distributions` directory. Extract the output and run the script inside the `bin` directory.