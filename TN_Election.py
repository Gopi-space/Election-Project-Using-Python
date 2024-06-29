import mysql.connector
import datetime as dt
import re
import smtplib




# Create a connection to the database
mydb=mysql.connector.connect(
  host='localhost',
  user='root',
  password='Gopi@2001',
  database='demo_db'
)


# Create a cursor object
mycursor = mydb.cursor()

def update_data():
    voters_mail=[]
    while True:
      name=input('enter your name: ')
      age=int(input('enter your age: '))
      mail=input('enter your mail id: ')
      voters_mail.append(mail)
      x=dt.datetime.now()
      if age>=18:
          print('you are eligible to vote')
          print('\nvote for gopi-1\nvote for mani-2\nvote for mohan-3\n')
          num=int(input('enter your candidiate no: '))
          
          if num==1:
              # Update the address
              mycursor.execute('update election set votes=votes+1 where name="gopi"')
              mydb.commit()  # Commit the changes to the database
          elif num==2:
              
              mycursor.execute('update election set votes=votes+1 where name="mani"')
              mydb.commit()  # Commit the changes to the database
          elif num==3:
              mycursor.execute('update election set votes=votes+1 where name="mohan"')
              mydb.commit()
          else:
              print('enter a valid num to vote')
      else:
          print('you are not eligible to vote')
      f=open('vote.txt','a')
      f.write(f'\nname: {name}\nage: {age}\n{x}\nthanks for voting...')
      

      try:
          for i in voters_mail:
              print(i,f'thanks for voting\n{x}')
              s=smtplib.SMTP('smtp.gmail.com',587)
              s.starttls()
              s.login('11062001gopinath@gmail.com','123455666')
              msg=(f'thanks for voting\n{x}')
              s.sendmail('11062001gopinath@gmail.com',i,msg)
              s.quit()
              print('mail sent to the voters')
      except:
          print('mail not sent')
      y=input('do you want to continue types yes : ')
      if y!='yes':
          break

def view_data():
    mycursor.execute('select * from election')
    myresult = mycursor.fetchall()  # Fetch all data from the database table

    for x in myresult:
        print(x)  

# Call the functions

update_data()
view_data()

# Close the cursor and connection
# mycursor.close()
# mydb.close()
