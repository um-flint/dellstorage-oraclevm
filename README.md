This code will read LUN information from a Dell Enterprise Manager using REST and then send the friendly name to Oracle VM so that you don't just see 'COMPELNT (1)', 'COMPELNT (2)'... as the disk names.

It can be run with './dellstorage-oraclevm.py' and expects a config file in the same directory named 'dellstorage-oraclevm.cfg'
