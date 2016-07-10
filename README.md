# abkfenris/postgis-pghoard

The `abkfenris/postgis-pghoard` image provides a Docker container running Postgres 9 with [PostGIS 2.2](http://postgis.net/) and [PGHoard](https://github.com/ohmu/pghoard) installed. This image is based on the [mdillon/postgis](https://hub.docker.com/r/mdillon/postgis/) image and provides variants for each version of Postgres 9 supported by the base image (9.1-9.5).



This image ensures that the default database created by the parent `postgres` image will have the `postgis` and `postgis_topology` extensions installed.  Unless `-e POSTGRES_DB` is passed to the container at startup time, this database will be named after the admin user (either `postgres` or the user specified with `-e POSTGRES_USER`). For Postgres 9.1+, the `fuzzystrmatch` and `postgis_tiger_geocoder` extensions are also installed.

If you would prefer to use the older template database mechanism for enabling PostGIS, the image also provides a PostGIS-enabled template database called `template_postgis`.

## Usage

This container can be run in one of two ways. Either it can back up another Postgres container, or it can restore from a backup, and then serve the Postgres database with backups allowed. The default method is to restore from backup.

### Restore from backup

Probably should add some information here.

### Backup a seperate database

Run the container with the command `pghoard --config PGHOARD_CONFIG_DIR` with `PGHOARD_CONFIG_DIR` pointing to your mounted config file.

### Environment Variables

- `PGHOARD_RESTORE_BASEBACKUP_CONFIG` - Full path to config file to restore basebackup from.
- `PGHOARD_RUNNING_CONFIG` - Full path to config file to use while Postgres is running.
- `PGHOARD_USER` - Replication user to allow PGHoard to connect.
- `PGHOARD_PASS` - Replication password to allow PGHoard to connect.
- `PGHOARD_HOSTNAME` - Replication host to allow PGHoard to connect.

### Volumes

PGHoard JSON config files should be mounted either as single files, or as a directory.  


In order to run a basic container capable of serving a PostGIS-enabled database, start a container as follows:

    docker run --name some-postgis -e POSTGRES_PASSWORD=mysecretpassword -d abkfenris/postgis-pghoard

For more detailed instructions about how to start and control your Postgres container, see the documentation for the [`postgres`](https://registry.hub.docker.com/_/postgres/) and [`postgis`](https://hub.docker.com/r/mdillon/postgis/) images.

Once you have started a database container, you can then connect to the database as follows:

    docker run -it --link some-postgis:postgres --rm postgres \
        sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

See [the PostGIS documentation](http://postgis.net/docs/postgis_installation.html#create_new_db_extensions) for more details on your options for creating and using a spatially-enabled database.
