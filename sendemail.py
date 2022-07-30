from multiprocessing import connection
import smtplib
from sqlite3 import connect
# just enter sender email  / password
my_email = ""
password = ""

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user= my_email , password= password)

recAdd = input("Please Enter reciepent email")
messg  = input("enter message ")
connection.sendmail(from_addr=my_email , to_addrs= recAdd , msg=messg )

connection.close()
