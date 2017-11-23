# lab lab exercise
# coding=utf-8
import MySQLdb as db
db1= db.connect(host="127.0.0.1",user="root", passwd="123456")
cursor=db1.cursor()
sql="CREATE SCHEMA IF NOT EXISTS lab"
cursor.execute(sql)

#create table STOCK
sql="""Create Table lab.STOCK(
       ID Int(11) Not Null,
       ticker VarChar(45) Not Null,
       exchange VarChar(45) Not Null,
       PRIMARY KEY (ID)
       );"""
#execute the sql query
cursor.execute(sql)


#create table PRICE
sql="""Create Table lab.PRICE(
        ID Int(11) Not Null,
        ticker VarChar(45) Not Null,
        date DATE Not Null,
        close FLOAT Not Null,
        PRIMARY KEY (ID)
        );"""
#execute the sql query
cursor.execute(sql)


#create table BUYnNSELL
sql="""Create Table lab.BUYNSELL(
        ID Int(11) Not Null,
        ticker VarChar(10) Not Null,
        buy_or_sell Enum("BUY","SELL") Not Null,
        date DATE Not Null,
        timestamp TIME Not Null,
        price FLOAT Not Null,
        num_of_shares Numeric(10) Not Null,
        PRIMARY KEY (ID)
        );"""
#execute the sql query
cursor.execute(sql)


# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO lab.STOCK
         VALUES (1,"AAPL","NASDAQ"),(2,"GOOG","NASDAQ"),(3,"MSFT","NASDAQ"),(4,"IBM","NYSE"), (5,"AMZN","NYSE")"""
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()


# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO lab.PRICE
        VALUES 
        (1,"AAPL","2017-03-20",100),(2,"AAPL","2017-03-21",101.5),(3,"AAPL","2017-03-22",106.5),
        (4,"GOOG","2017-03-20",100),(5,"GOOG","2017-03-21",130),(6,"GOOG","2017-03-22",110),
        (7,"MSFT","2017-03-20",184.5),(8,"MSFT","2017-03-21",188.5),(9,"MSFT","2017-03-22",210),
        (10,"IBM","2017-03-20",72),(11,"IBM","2017-03-21",70),(12,"IBM","2017-03-22",10),
        (13,"AMZN","2017-03-20",882),(14,"AMZN","2017-03-21",885),(15,"AMZN","2017-03-22",894)"""
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()


# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO lab.BUYnSELL
         VALUES (1,"IBM", "BUY", "2017-03-20","11:55:00",273,1100),(2,"IBM", "BUY", "2017-03-21","10:45:00",271,2400),(3,"IBM", "SELL", "2017-03-22","12:09:00",270.5,2500),
         (4,"GOOG", "BUY", "2017-03-20","12:22:00",86,2200),(5,"GOOG", "SELL", "2017-03-20","14:00:00",87,1000),(6,"GOOG", "SELL", "2017-03-21","10:22:00",87.5,1000),(7,"GOOG", "BUY", "2017-03-21","13:28:00",87,800),(8,"GOOG", "SELL", "2017-03-22","11:45:00",86,500),
         (9,"AAPL", "BUY", "2017-03-20","10:01:00",99,1000),(10,"AAPL", "BUY", "2017-03-20","11:22:00",99.5,1000),(11,"AAPL", "BUY", "2017-03-21","14:22:00",100,1000),(12,"AAPL", "SELL", "2017-03-22","14:42:00",103,3000),
         (13,"MSFT", "BUY", "2017-03-20","11:45:00",186,1500),(14,"MSFT", "SELL", "2017-03-21","10:45:00",188,1000),(15,"MSFT", "BUY", "2017-03-22","12:03:00",187,5000),
         (16,"AMZN", "BUY", "2017-03-20","11:55:00",883,100),(17,"AMZN", "BUY", "2017-03-21","12:05:00",886,100),(18,"AMZN", "SELL", "2017-03-22","14:45:00",894,200)"""
#Exception handling using try and expect
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db1.commit()
except:
   # Rollback in case there is any error
   db1.rollback()


#Q1
print "Q1"
# Prepare SQL query to fetch records.
sql = """SELECT S.ticker,P.close FROM lab.STOCK S, lab.PRICE P 
WHERE (S.ticker= P.ticker AND year(P.date)="2017")"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()

   for row in results:
      ticker = row[0]
      close = row[1]
      # Now print fetched result
      print "Ticker =", ticker, " Close =",close

except:
   print "Error: unable to fetch data"


#Q2
print "Q2"
# Prepare SQL query to fetch records.
sql = """SELECT distinct P.ticker FROM lab.PRICE P, lab.PRICE I, lab.PRICE G 
WHERE (P.date="2017-03-20" AND  I.date="2017-03-20" AND I.ticker= "IBM" AND P.close>I.close)"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ticker = row[0]
      # Now print fetched result
      print "Ticker =", ticker

except:
   print "Error: unable to fetch data"


#Q3
print "Q3"
# Prepare SQL query to fetch records.
sql = """SELECT distinct P.ticker FROM lab.PRICE P 
WHERE P.close= (SELECT Max(A.close) From lab.PRICE A  WHERE A.date= '2017-03-20')"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ticker = row[0]
      # Now print fetched result
      print "Ticker =", ticker

except:
   print "Error: unable to fetch data"


#Q4
print "Q4"
# Prepare SQL query to fetch records.
sql = """SELECT distinct S.ticker FROM lab.STOCK S, lab.PRICE P 
WHERE S.ticker=P.ticker AND P.date="2017-03-20" AND S.exchange= "NYSE" AND (P.close<20 OR P.close>100 )"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ticker = row[0]
      # Now print fetched result
      print "Ticker =", ticker


except:
   print "Error: unable to fetch data"


#Q5
print "Q5"
# Prepare SQL query to fetch records.
sql = """SELECT DISTINCT P.ticker FROM lab.STOCK S, lab.PRICE P, lab.PRICE A, lab.PRICE B
WHERE S.exchange= "NYSE"  AND P.ticker= S.ticker 
AND P.close > 100 AND year(P.date)='2017'
AND (A.close-B.close)= (Select Max(A.close-B.close) FROM lab.PRICE A, lab.PRICE B, lab.STOCK S WHERE A.ticker = S.ticker AND B.ticker= S.ticker 
AND A.date ='2017-03-20' AND B.date ='2017-03-21' AND S.exchange='NYSE')"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      ticker = row[0]
      # Now print fetched result
      print "Ticker =", ticker
except:
   print "Error: unable to fetch data"


#Q6
print "Q6"
# Prepare SQL query to fetch records.
sql = """SELECT DISTINCT B.date FROM lab.BuynSELL B
WHERE B.ticker= "AAPL"  AND B.buy_or_sell="SELL" 
AND (B.price* B.num_of_shares) > (SELECT SUM(C.price* C.num_of_shares) AS Total From lab.BuynSELL C 
WHERE C.ticker IN (SELECT D.ticker From lab.STOCK D WHERE D.exchange= "NASDAQ" AND D.ticker= "AAPL")
AND C.buy_or_sell="BUY")"""


try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      date = row[0]
      # Now print fetched result
      print "Date =", date
except:
   print "Error: unable to fetch data"



# disconnect from server
db1.close()
