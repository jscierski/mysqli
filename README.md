# mysqli
This is `mysql` improved. A slightly better MySQL command line client.

# Getting started

`pip install mysqli` should do the trick.

# Feature List

Here's a very thorough rundown of the wonderful things you can do with `mysqli` by your side.

| You do      | This happens           | How cool  |
| --------- |:------:| ---:|
| `\dt`      | `SHOW TABLES` | Very |
| `\ds`      | `SHOW DATABASES`      |   Okay |
| `\dp`      | `SHOW PROCESSLIST`      |   Okay |
| `$tablename` | `SELECT * FROM $tablename` | Very |
| `@innodb_` | `SHOW GLOBAL VARIABLES LIKE 'innodb_%'` | Radical |
| `@innodb_something=1` | `SET GLOBAL @innodb_something=1` | Radical |
| `$tablename.first` | First row in `$tablename` | Lame |
| `$tablename.last` | Last row in `$tablename` | So-so |
| $table1+$table2 | `JOIN` these two tables | Cute, but dumb |
| run with `--gay` | Dynamic rainbow prompt | 90s cool |
| `dump` | `mysqldump` current database into `~` | Very |

# Gotchas

This is version `0.x`, however we do use it internally in place of the stock `mysql` command ("in place" may not be the right word seeing how `mysqli` basically acts as a proxy to `mysql`). You can't really use session variables, since you get a new session for every command. Also, many things are still just a random ideas with minimal time spent on implementation.

# Roadmap

We keep using it, you start using it, feedback happens and over time we actually build something nice. 

# About exana.io
We believe in giving back. It's easy to forget we wouldn't be here without the crazy idea of sharing your work.

# License
Licensed under the Apache License, Version 2.0. 
