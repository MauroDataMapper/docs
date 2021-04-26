A tool has been built to migrate data from old instances of Metadata Catalogue to Mauro Data Mapper.  This is a docker-based tool which applies a 
number of SQL scripts to move data into a new database schema, and transform the data into a new format suitable for Mauro.

The GitHub repository for the migration is here: 
[https://github.com/MauroDataMapper/mc-to-mdm-migration](https://github.com/MauroDataMapper/mc-to-mdm-migration).

## Manual Process

Please see the documents in the `guide` folder for further information.

## Automated Process

You can use one of the 2 available scripts in the top of the repository to run the migration from start to finish

You have 2 options as with the manual process documents, depending on if you're running Metadata Catalogue and Mauro Data Mapper inside or
outside Docker.

The scripts execute the stages described in the guide, so if you're unsure as to what parameters you should feed in then please read the guides
to find out more.

The scripts all execute using the defaults as if you have built the system using Docker

### Docker Based PostgreSQL
```bash
# Help/Usage
./run-complete-migration-docker.sh --help
# Default parameters run
./run-complete-migration-docker.sh
```

### Remote/Local PostgreSQL

```bash
# Help/Usage
./run-complete-migration-remote.sh --help
# Default parameters run
./run-complete-migration-remote.sh
```

## Notes

Please be aware that DataFlows are currently not migrated using this system, and may need to be manually migrated, or exported / imported.

