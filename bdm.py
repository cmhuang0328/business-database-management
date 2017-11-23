#!/usr/bin/env python
import cgi, cgitb
import MySQLdb

# connect to the database
db = MySQLdb.connect("localhost","root","123456","lab" )

# setup a cursor object using cursor() method
cursor = db.cursor()

form = cgi.FieldStorage()
text_content = form.getvalue('textcontent')

sql=text_content

try:   
	cursor.execute(sql)  
	results = cursor.fetchall()  
	attribute = cursor.description   
except:
	print "Error"

# run a sql question
#cursor.execute("SELECT max(close) from lab.PRICE")
# grab one result
#data = cursor.fetchall()

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>";
print "<title>Lab</title>"
print "</head>"
print "<body>"
#print "<h2> %s</h2>" % results
print "<table>"
print "<tr>"
col_name_list=[tuple[0] for tuple in attribute]
#colnamestring=', '.join(map(str,col_name_list))
#print "<h2>{0}</h2>".format(colnamestring)
for col in col_name_list:
 print "<th>{0}</th>".format(col)
print "</tr>"
for row in results:
# mystring=', '.join(map(str,row))
# print "<h2>{0}</h2>" .format(mystring)
 print "<tr>"
 for col in row:
  print "<td>{0}</td>".format(col)
 print"</tr>"
print "</table>"
print "</body>"
print "</html>"

# close the mysql database connection
db.close()