def create(x,y,z):
  global g
  g="{}_{}".format(y,z)
  print("Table name:",g)
  q="create table {}(Roll_Number int(10) not null,Name varchar(20) not null,Maths decimal(65,2),Physics decimal(65,2),Chemistry decimal(65,2),English decimal(65,2))".format(g)
  c.execute(q)
  for i in range(x):
    n=int(input("Enter roll_number:"))
    m=input("Enter name:")
    m.capitalize()
    e=int(input("Enter Maths Marks:"))
    f=int(input("Enter Physics Marks:"))
    w=int(input("Enter Chemistry Marks:"))
    s=int(input("Enter English Marks:"))
    y="insert into {} values({},'{}',{},{},{},{})".format(g,n,m,e,f,w,s)
    c.execute(y)
    mycon.commit()
def update(x,y):
    for i in range(y):
     n=int(input("Enter roll_number:"))
     m=input("Enter name:")
     m.capitalize()
     e=int(input("Enter Maths Marks:"))
     f=int(input("Enter Physics Marks:"))
     w=int(input("Enter Chemistry Marks:"))
     s=int(input("Enter English Marks:"))
     y="insert into {} values({},'{}',{},{},{},{})".format(x,n,m,e,f,w,s)
     c.execute(y)
     mycon.commit()
def donutper():   
  r='y'
  while r=='y':
   print("reviewing the performance of a students")
   import matplotlib.pyplot as plt
   n=input("Enter subject:")
   l=[]
   q="select count(*) from {} where {} > 90".format(g,n)
   c.execute(q) 
   d=c.fetchone()
   l.append(d[0])
   q="select count(*) from {} where {} between 80 and 90".format(g,n)
   c.execute(q) 
   d=c.fetchone()
   l.append(d[0])
   q="select count(*) from {} where {} between 60 and 80".format(g,n)
   c.execute(q) 
   d=c.fetchone()
   l.append(d[0])
   q="select count(*) from {} where {} < 60".format(g,n)
   c.execute(q) 
   d=c.fetchone()
   l.append(d[0])
   sizes=l
   label=['90 and above','between 80 and 90','between 60 and 80','below 60']
   plt.pie(sizes,labels=label,autopct='%1.1f%%')
   plt.axis('equal')
   circle=plt.Circle(xy=(0,0), radius=0.75,facecolor='white')
   plt.gca().add_artist(circle)
   plt.title(n)
   plt.show()
   r=input('do you want to review another subject(y/n):')
  else:
      mycon.close()
      print("thank you!!!")

#__main__
import pymysql as sql
mycon=sql.connect(host='localhost',user='root',password='appleandknife',database='school')
c=mycon.cursor()
r=input("does the table exists(y/n):")
if r=='y':
 s=input("do you want to add rows(y/n):")
 if s=='y':
    g=input("table name:")
    l=int(input("Enter number of students to be added:"))
    update(g,l)
else:
  l=int(input("Enter number of students in class:"))
  k=(input("enter class:"))
  u=int(input("Enter year:"))
  create(l,k,u)
hg=input("do you want you review performance of students(y/n)?")
if hg=='y':
    g=input("table name:")
    donutper()
else:
    print("Thank you!!!")
