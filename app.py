from flask import Flask, render_template, request, redirect
import matplotlib.pyplot as plt
from flask_sqlalchemy import SQLAlchemy
from matplotlib.figure import Figure
import base64
from io import BytesIO


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///markList.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class markList(db.Model):
    rollno = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    math = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)
    science = db.Column(db.Integer, nullable=False)
    sst = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"{self.rollno}-{self.name}"
    

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        # rollno = request.form['rollno']
        name=request.form['name']
        math=request.form['math']
        english=request.form['english']
        science = request.form['science']
        sst = request.form['sst']
        marks = markList(name=name, math=math, english=english, science=science, sst=sst)
        db.session.add(marks)
        db.session.commit()
    return render_template('index.html')

@app.route("/marksheet")
def marksheet():
    markSheet= markList.query.all()
    print(markSheet)
    return render_template('marksheet.html', markSheet=markSheet)


@app.route("/update/<int:rollno>", methods=['GET', 'POST'])
def update(rollno):
    if request.method=="POST":
        # rollno=request.form['rollno']
        name=request.form['name']
        math=request.form['math']
        english=request.form['english']
        science = request.form['science']
        sst = request.form['sst']
        mark = markList.query.filter_by(rollno=rollno).first()
        # mark.rollno = rollno
        mark.name = name
        mark.math=math
        mark.english=english
        mark.science=science
        mark.sst=sst
        db.session.add(mark)
        db.session.commit()
        return redirect("/marksheet")
    mark = markList.query.filter_by(rollno=rollno).first()
    return render_template('update.html', mark=mark)
    
@app.route("/delete/<int:rollno>")
def delete(rollno):
    mark = markList.query.filter_by(rollno=rollno).first()
    db.session.delete(mark)
    db.session.commit()
    return redirect('/marksheet')

@app.route("/donuts", methods=['GET','POST'])
def donuts():
    if request.method=="POST":
        label=['90 and above','between 80 and 90','between 60 and 80','below 60']
        values=[]
        flag=1;
        subject=request.form['subjects']
        print(subject)
        if subject=="math":
            values.append(db.session.query(markList).filter(markList.math>= 90).count())
            values.append(db.session.query(markList).filter(markList.math>=80).filter(markList.math<90).count())
            values.append(db.session.query(markList).filter(markList.math>=60).filter(markList.math<80).count())
            values.append(db.session.query(markList).filter(markList.math<60).count())
            print(values)
        elif subject=="english":
            values.append(db.session.query(markList).filter(markList.english>= 90).count())
            values.append(db.session.query(markList).filter(markList.english>=80).filter(markList.english<90).count())
            values.append(db.session.query(markList).filter(markList.english>=60).filter(markList.english<80).count())
            values.append(db.session.query(markList).filter(markList.english<60).count())
            print(values)
        elif subject=="science":
            values.append(db.session.query(markList).filter(markList.science>= 90).count())
            values.append(db.session.query(markList).filter(markList.science>=80).filter(markList.science<90).count())
            values.append(db.session.query(markList).filter(markList.science>=60).filter(markList.science<80).count())
            values.append(db.session.query(markList).filter(markList.science<60).count())
            print(values)
        else:
            subject="socail science"
            values.append(db.session.query(markList).filter(markList.sst>= 90).count())
            values.append(db.session.query(markList).filter(markList.sst>=80).filter(markList.sst<90).count())
            values.append(db.session.query(markList).filter(markList.sst>=60).filter(markList.sst<80).count())
            values.append(db.session.query(markList).filter(markList.sst<60).count())
            print(values)
        label=['90 and above','between 80 and 90','between 60 and 80','below 60']
        print("values: ", values)
        plt.pie(values,labels=label,autopct='%1.1f%%')
        plt.axis('equal')
        circle=plt.Circle(xy=(0,0), radius=0.75,facecolor='white')
        plt.gca().add_artist(circle)
        plt.title(subject.capitalize())
        plt.legend(loc ="best")
        buf = BytesIO()
        plt.savefig(buf, format="png") 
        # plt.show()
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        plt.close()
        return render_template('donut.html', data=data, flag=flag)
    flag=0
    return render_template('donut.html', flag=flag)


if __name__ == "__main__":
    app.run(debug=True, port=8000)