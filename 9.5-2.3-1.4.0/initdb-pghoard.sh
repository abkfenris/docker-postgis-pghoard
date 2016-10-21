#!/bin/sh
set -e

echo "Configuring database to accept pghoard backups."

file="$PGDATA/postgresql.conf"

cat >> $file <<-EOT
wal_level = archive
max_wal_senders = 4
archive_timeout = 300
EOT 

cat $file

#echo "host    REPLICATION     $PGHOARD_USER   $PGHOARD_HOSTNAME       md5" >> /var/lib/postgresql/data/pg_hba.conf

file="$PGDATA/pg_hba.conf"

# works to insert, but doesn't replace env variables
#sed -i 's/host.*0\/0.*trust/host replication $PGHOARD_USER $PGHOARD_HOSTNAME md5\n&/' $file

sed -i 's@host.*0/0.*md5@host replication '$PGHOARD_USER' '127.0.0.1/32' md5\n&@' $file

cat $file

"${psql[@]}" --username $POSTGRES_USER -v ON_ERROR_STOP=1 <<-EOSQL
  CREATE USER "$PGHOARD_USER" WITH PASSWORD '$PGHOARD_PASS' REPLICATION;
  SELECT pg_reload_conf();
EOSQL


