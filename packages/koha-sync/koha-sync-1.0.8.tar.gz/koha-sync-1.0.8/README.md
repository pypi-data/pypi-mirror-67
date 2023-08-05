# Koha synchronizer #

This projects allows us to a script to synchronize Koha rows from a remote database to our Elasticsearch cluster.  

Run the command
```yml
koha_syncrhonizer --help

    Options:
     -c, --config-file TEXT  path to configuration file  [required]
     -v, --verbose           activate verbosity output
     -r, --run-once          synchronize once and stops execution
     -t, --test              run validations and stops before synchronize
     --help                  Show this message and exit.

```