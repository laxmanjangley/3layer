# 3layer
DBMS assignment 1

1. Implement part of 3 level architecture which should accept
- 	Definition of schemas (which defines names of files and record structures with given attributes
	and length’s together with keys)
	and should output
- 	Definition of data structure (of files) to store (or manage) the data as described in the schema.
2. Implement subschema definition which should accept
- 	Definition of subschema which is a subset of the defined schema
	and do the following
- 	Check for correctness that subschema has been defined properly
- 	Create view structures against which DML’s can operate against the subschema.


Format of files:
1.
number of tables
name of table1
number of attribute in table1
( attribute1,type,isKey)
( attribute2,type,isKey)
.
.
.
number of records in table1
record1
record2
.
.
.
name of the table 2
.
.
.
number of key relations
relation1
relation2
.
.
2.
number of attributes in the subschema
(table name,attribute)
.
.
.