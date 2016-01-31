#!/usr/bin/python
import sys
import datetime
def date(s):
	d = s.split('/');
	if not(len(d)==3) :
		raise ValueError('Specify date in the correct format');
	return datetime.date(int(d[2]),int(d[1]),int(d[0]));
input = open(sys.argv[1]);
types ={"FLOAT":float,"INTEGER":int,"STRING":str,"BOOLEAN":bool,"REAL":float,"DATE":datetime.date,"TIME":datetime.date,"CURRENCY":float};
prim_key = {};
dict = {};
valid = {};
table_keys = {};
tables = [];
no_of_tables = int(input.readline());
while no_of_tables > 0:
	table = input.readline().strip("\n");
	tables.append(table);
	table_keys[table] = [];
	format = {};
	valid[table] = True;
	no_of_attr = int(input.readline().strip("()\n"));
	flag = 0;
	dict[table] = [];
	while no_of_attr > 0:
		vals = input.readline().strip("()\n").split(',');
		format[vals[0]] = types[vals[1]];
		table_keys[table].append(vals[0]);
		if vals[2] == "1":
			flag += 1;
			prim_key[table] = vals[0];
		no_of_attr -=1;
	if flag >1:
		print "Too many primary keys defined for table {}.\n".format(table);
		valid[table] = False;
	no_of_records = int(input.readline().strip("()\n"));
	while no_of_records > 0:
		vals = input.readline().strip("()\n").split(',');
		dictr = {};
		if(len(vals) != len(table_keys[table])):
			print "Incorrect specification of attributes in {}\n".format(table);
			valid[table] = False;
			break;
		for i in range(0,len(vals)):
			try:
				if(table_keys[table][i] == "DATE"):
					dictr[table_keys[table][i]] = date(vals[i]);
				elif(table_keys[table][i] == "TIME"):
					dictr[table_keys[table][i]] = datetime.datetime.strptime(vals[i],'%H:%M:%S');
				elif(table_keys[table][i] == "CURRENCY"):
					dictr[table_keys[table][i]] = (vals[i].split()[0],int(vals[i].split()[1]));					
				else:
					dictr[table_keys[table][i]] = format[table_keys[table][i]](vals[i]);
			except ValueError:
				print "TypeError {}:{} specified as {}\n".format(table,table_keys[table][i],format[table_keys[table][i]]);
				valid[table] = False;
				break;
		dict[table].append(dictr);
		no_of_records -= 1;
	no_of_tables-=1;
for (key,value) in dict.items():
	try:
		x = prim_key[key];
		for l in dict[key]:
			for m in dict[key]:
				if(l!=m):
					if l[x] == m[x]:
						valid[key] = False;
	except KeyError:
		s = "";
no_of_relationships = int(input.readline());
while no_of_relationships > 0:
	relation = "";
	x = input.readline();
	flag = 0;
	for c in x:
		if not(c == '(' or c == ')' or c == '\n'):
			relation += c;
	vals = relation.split(',');
	if not(valid[vals[0]] and valid[vals[2]]):
		valid[vals[0]] = False;
		valid[vals[2]] = False;
	for i in dict[vals[2]]:
		for j in dict[vals[0]]:
			if j[vals[1]] == i[vals[3]]:
				flag = 1;
		if flag == 0:
			print "Invalid relationship {}. {}:{} does not contain entry corresponding to {}:{}:{}\n".format(x,vals[0],vals[1],vals[2],vals[3],i[vals[3]]);
			valid[vals[0]] = False;
			valid[vals[2]] = False;
			break;
	no_of_relationships -=1;
f = open(sys.argv[2],'w');
for (key,value) in dict.items():
	if not(valid[key]):
		del dict[key];
		f.write("{}\nInvalid\n".format(key));
for i in dict:
	print i;
	f.write("{}\n".format(i));
	for j in dict[i]:
		klist = j.keys();
		klist.sort();
		for k in klist:
			print "{},\t".format(j[k]),
			f.write("{},\t".format(j[k]));
		print '\n';
		f.write('\n');
