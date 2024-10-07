from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Compreg.db'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

class Compreg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Company_Name=db.Column(db.String(20),unique=False,nullable=False)
    Company_Type=db.Column(db.String(20),unique=False,nullable=False)
    Passkey=db.Column(db.String(20),unique=False,nullable=False)

    def __repr__(self):
        return f"Name:{self.Company_Name}{self.Company_Type}{self.Passkey}"
    

@app.route('/')
def getstart():
    return render_template('get.html')
    
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/mainreg')
def mainreg():
    return render_template('register.html')

@app.route('/compreg',methods=['POST','GET'])
def compreg():
    if request.method=='POST':
        Company_Name=request.form.get("Company_Name")
        Company_Type=request.form.get("Company_Type")
        Passkey=request.form.get("Passkey")
        if Company_Name!='' and Company_Type!='' and Passkey!='':
            p=Compreg(Company_Name=Company_Name,Company_Type=Company_Type,Passkey=Passkey)
            db.session.add(p)
            db.session.commit()
            return redirect('/complog')
        else:
            return redirect(url_for('compreg'))
    else:
        return render_template('compreg.html')

@app.route('/complog',methods=['POST','GET'])
def comp():
    if request.method=='POST':
        Company_Name=request.form.get("Company_Name")
        Passkey=request.form.get("Passkey")

        a=Compreg.query.filter_by(Company_Name=Company_Name,Passkey=Passkey).first()
        if Company_Name!='' and Passkey!='':
            a=Compreg(Company_Name=Company_Name,Passkey=Passkey)
            return redirect('comprof')
        else:
            return "Error"
    else:
        return render_template('complog.html')
        

@app.route('/comprof')
def comprof():
    # if request.method=='POST':
    #     return redirect(url_for('comprof'))
    return render_template('comprof.html')

@app.route('/compinfo')
def compinfo():
    return render_template('compinfo.html')

#===========================================================================================================#



class Empreg(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Employee_Name=db.Column(db.String(20),unique=False,nullable=False)
    Employee_Email=db.Column(db.String(20),unique=False,nullable=False)
    Phone_Number=db.Column(db.Integer,unique=False,nullable=False)
    Password=db.Column(db.String(20),unique=False,nullable=False)
    Company_Passkey=db.Column(db.String(20),unique=False,nullable=False)    

    def __repr__(self):
        return f"Name:{self.Employee_Name}{self.Employee_Email}{self.Phone_Number}{self.Password}{self.Company_Passkey}"
    

@app.route('/index')
def index():
    users=Empreg.query.all()
    return render_template('empdata.html',EmpUser=users)

@app.route('/empreg',methods=['POST','GET'])
def empreg():
    if request.method=='POST':
        Employee_Name=request.form.get("Employee_Name")
        Employee_Email=request.form.get("Employee_Email")
        Phone_Number=request.form.get("Phone_Number")
        Password=request.form.get("Password")
        Company_Passkey=request.form.get("Company_Passkey")

        if Employee_Name!='' and Employee_Email!='' and Phone_Number!='' and Password!='' and Company_Passkey!='':
            p=Empreg(Employee_Name=Employee_Name,Employee_Email=Employee_Email,Phone_Number=Phone_Number,Password=Password,Company_Passkey=Company_Passkey)
            db.session.add(p)
            db.session.commit()
            return redirect (url_for('emplog'))
        # else:
        #     return redirect(url_for('empreg'))
    else:
        return render_template('empreg.html')


@app.route('/emplog',methods=['POST','GET'])
def emplog():
    if request.method=='POST':
        Employee_Name=request.form.get("Employee_Name")
        Password=request.form.get("Password")

        p=Empreg.query.filter_by(Employee_Name=Employee_Name,Password=Password).first()
        if Employee_Name!='' and Password!='':
            return redirect (url_for('emprof'))
        # else:
        #     return redirect(url_for('emplog'))
    else:
        return render_template('emplog.html')

@app.route('/emprof',methods=['POST','GET'])
def emprof():
    return render_template('emprof.html')

@app.route('/index2')
def index2():
    users1=Empreg.query.all()
    return render_template('empinfo.html',EmpInfo=users1)

# @app.route('/empinfo')
# def empinfo():
#     return render_template('empinfo.html')

@app.route('/empinfo',methods=['POST','GET'])
def data():
    if request.method=='POST':
        Employee_Name=request.form.get("Employee_Name")
        Employee_Email=request.form.get("Employee_Email")
        Phone_Number=request.form.get("Phone_Number")

        q=Empreg.query.filter_by(Employee_Name=Employee_Name,Employee_Email=Employee_Email,Phone_Number=Phone_Number,).first()
        if Employee_Name!='' and Employee_Email!='' and Phone_Number is not None:
            return redirect (('/index2'))
        # else:
        #     return redirect(url_for('empinfo'))
    else:
        return render_template('empinfo.html')

#===============================================================================

class Empleaveapp(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Employee_Name=db.Column(db.String(20),unique=False,nullable=False)
    department=db.Column(db.String(20),unique=False,nullable=False)
    Phone_Number=db.Column(db.Integer,unique=False,nullable=False)
    # password=db.Column(db.String(20),unique=False,nullable=False)
    Employee_Email=db.Column(db.String(20),unique=False,nullable=False)
    emergencyLeave=db.Column(db.String(20),unique=False,nullable=True)
    annualLeave=db.Column(db.String(20),unique=False,nullable=True)
    sickLeave=db.Column(db.String(20),unique=False,nullable=True)
    maternityLeave=db.Column(db.String(20),unique=False,nullable=True)
    otherLeave=db.Column(db.String(20),unique=False,nullable=True)

    def __repr__(self):
        return f"Name:{self.Employee_Name}{self.department}{self.Phone_Number}{self.Employee_Email}{self.emergencyLeave}{self.annualLeave}{self.sickLeave}{self.maternityLeave}{self.otherLeave}"


@app.route('/index1')
def index1():
    user=Empleaveapp.query.all()
    return render_template('empreqdata.html',Empleave=user)

# @app.route('/request')
# def empreq():
#     return render_template('leave.html')

@app.route('/request', methods=['POST', 'GET'])
def reqdata():
    if request.method == "POST":
        Employee_Name = request.form.get("Employee_Name")
        department = request.form.get("department")
        Phone_Number = request.form.get("Phone_Number")
        Employee_Email = request.form.get("Employee_Email")
        emergencyLeave = request.form.get("emergencyLeave")
        annualLeave = request.form.get("annualLeave")
        sickLeave = request.form.get("sickLeave")
        maternityLeave = request.form.get("maternityLeave")
        otherLeave = request.form.get("otherLeave")

        # Check for required fields
        if all([Employee_Name, department, Phone_Number, Employee_Email, emergencyLeave, annualLeave, sickLeave, maternityLeave, otherLeave]):
            r = Empleaveapp(
                Employee_Name=Employee_Name,
                department=department,
                Phone_Number=Phone_Number,
                Employee_Email=Employee_Email,
                emergencyLeave=emergencyLeave,
                annualLeave=annualLeave,
                sickLeave=sickLeave,
                maternityLeave=maternityLeave,
                otherLeave=otherLeave
            )
            db.session.add(r)
            db.session.commit()
            return redirect(url_for('appdec'))
        # else:
        #     return redirect(url_for('reqdata'))  # Redirect back to the form if validation fails
    else:
        return render_template('leave.html')
    

@app.route('/appdecs')
def appdec():
    return render_template('appdec.html')

@app.route('/suc')
def Success():
    return render_template('approve.html')

@app.route('/dec')
def Failure():
    return render_template('decline.html')

# @app.route('/request',methods=['POST','GET'])
# def reqdata():
#     if request.method=="POST":
#         Employee_Name=request.form.get("Employee_Name")
#         department=request.form.get("department")
#         Phone_Number=request.form.get("Phone_Number")
#         Employee_Email=request.form.get("Employee_Email")
#         emergencyLeave=request.form.get("emergencyLeave")
#         annualLeave=request.form.get("annualLeave")
#         sickLeave=request.form.get("sickLeave")
#         maternityLeave=request.form.get("maternityLeave")
#         otherLeave=request.form.get("otherLeave")

#         r=Empleaveapp.query.filter_by(Employee_Name=Employee_Name,department=department,Phone_Number=Phone_Number,Employee_Email=Employee_Email,emergencyLeave=emergencyLeave,annualLeave=annualLeave,sickLeave=sickLeave,maternityLeave=maternityLeave,otherLeave=otherLeave).first()
#         if Employee_Name!='' and department!='' and Phone_Number!='' and Employee_Email!='' and emergencyLeave!='' and annualLeave!='' and sickLeave!='' and maternityLeave!='' and otherLeave!='':
#             r=Empleaveapp(Employee_Name=Employee_Name,department=department,Phone_Number=Phone_Number,Employee_Email=Employee_Email,emergencyLeave=emergencyLeave,annualLeave=annualLeave,sickLeave=sickLeave,maternityLeave=maternityLeave,otherLeave=otherLeave)
#             db.session.add(r)
#             db.session.commit()
#             return redirect (('/comprof'))
#         # else:
#         #     return redirect(url_for('/comprof'))
#     else:
#         return render_template('leave.html')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)