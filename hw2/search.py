import mysql.connector
import sys

name = sys.argv[1]

cnx = mysql.connector.connect(user='root',password='Dsci-551',host='192.168.31.55',database='sakila')
# Since I use the linux system on my own local computer to install mysql, and I can’t  guarantee that my computer is always on power
# and data can be accessed through my ip at anytime. Therefor, I attach a sreenshot of some running samples in the submissions. 
cursor = cnx.cursor()
query = "select s.first_name,s.last_name,t.city from (select first_name,last_name,address_id from customer where first_name="+name+") as s,(select m.address_id, n.city from address m,city n where m.city_id=n.city_id) as t where s.address_id = t.address_id"
cursor.execute(query)
for res in cursor:
    print(res)

cursor.close()
cnx.close()