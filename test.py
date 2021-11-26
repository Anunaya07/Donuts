from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
from flask_sqlalchemy import SQLAlchemy
from matplotlib.figure import Figure
import base64
from io import BytesIO

for i in [[7,8,4,5],[10,8,5,6]]:
     label=['90 and above','between 80 and 90','between 60 and 80','below 60']
     values = i
     plt.pie(values,labels=label,autopct='%1.1f%%')
     plt.axis('equal')
     circle=plt.Circle(xy=(0,0), radius=0.75,facecolor='white')
     plt.gca().add_artist(circle)
     buf = BytesIO()
     plt.savefig(buf, format="png") 
     plt.show()
     data = base64.b64encode(buf.getbuffer()).decode("ascii")
    #  print(data)
     buf.flush()
     buf.seek(0)