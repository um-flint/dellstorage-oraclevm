This code will read LUN information from Dell Storage Enterprise Manager using REST and then send the friendly name to Oracle VM so that you don't just see 'COMPELNT (1)', 'COMPELNT (2)'... as the disk names.

It can be run with './dellstorage-oraclevm.py' and expects a config file in the same directory named 'dellstorage-oraclevm.cfg'

It was written on a Mac with Python 2.7.

I have tested it with:
* Dell Storage Enterprise Manager 2015 R3
* Dell Storage Manager 2016 R3
* Oracle VM Manager 3.3.4
* Oracle VM Manager 3.4.3
