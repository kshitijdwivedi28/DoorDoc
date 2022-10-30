import doctest
from email import policy
from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView

from CameraIntegration.views import symptom
from .form import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Appointment, User
from fpdf import FPDF


def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if(user.is_customer):
                    login(request,user)
                    return redirect('/accounts/user')
                else:
                    login(request,user)
                    return redirect('/accounts/user')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')
def user(request):
    dict={"Key":"yes","Value":{}}
    q=Appointment.objects.all()
    for i in q:
        fee=500
        if(i.policy != None):
            fee=200
        if(i.coupon ==''):
            fee=None
        dict2={"name":i.name,"email":i.email,"phone":i.phone,"aadhar":i.aadhar,"policy":i.policy,
        "coupon":i.coupon,"date":i.appointment_date,"department":i.department,"doctor":i.doctor,
        "message":i.message,"symptom":i.symptoms,"fees":fee}
        dict["Value"][i]=dict2
        dict["fees"]=fee
    print(dict)
    naam=None
    email=None
    phone=None
    policy=None
    aadhar=None
    coupon=None
    dt=None
    department=None
    doctor=None
    message=None
    res=request.POST
    result = request.POST
    for i in result:
        if naam ==None:
            dict["Key"]="no"
        if i=='name':
            naam=res[i]
        if i=='email':
            email=res[i]
        if i=='phone':
            phone=res[i]
        if i=='policy':
            policy=res[i]
        if i=='aadhar':
            aadhar=res[i]
        if i=='coupon':
            coupon=res[i]
        if i=='date':
            dt=res[i]
        if i=='coupon':
            coupon=res[i]
        if i=='department':
            department=res[i]
        if i=='doctor':
            doctor=res[i]
        if i=='message':
            message=res[i]
    if(naam is not None and doctor is not None):
        pdf = FPDF()  
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = "GetADoc", ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "________________________________________________________________________________________________________________________",ln = 2, align = 'L')
        pdf.cell(200, 10, txt = "Unique Appointment ID : "+phone+aadhar,ln = 2, align = 'C')
        pdf.cell(200, 10, txt = "________________________________________________________________________________________________________________________",ln = 3, align = 'L')
        pdf.cell(200, 10, txt = "Name : "+naam,ln = 4, align = 'L')
        pdf.cell(200, 10, txt = "Email : "+email,ln = 5, align = 'L')
        pdf.cell(200, 10, txt = "Contact No : "+phone,ln = 6, align = 'L')
        pdf.cell(200, 10, txt = "Policy ID : "+policy,ln = 9, align = 'L')
        pdf.cell(200, 10, txt = "Aadhar : "+aadhar,ln = 9, align = 'L')
        pdf.cell(200, 10, txt = "Date of Appointment: "+dt,ln = 7, align = 'L')
        pdf.cell(200, 10, txt = "Department : "+department,ln = 8, align = 'L')
        pdf.cell(200, 10, txt = "Doctor : "+doctor,ln = 9, align = 'L')
        pdf.cell(200, 10, txt = "________________________________________________________________________________________________________________________",ln = 3, align = 'L')
        pdf.cell(200, 10, txt = "Message : "+message,ln = 10, align = 'L')
        f = open("demofile2.txt", "r")
        str=f.readlines()
        print(str)
        str1 = "" 
        for ele in str: 
            str1 += ele  
        pdf.cell(200, 10, txt = "Symptoms: "+str1,ln =11, align = 'L')
        f.close()
        q=Appointment(name=naam,email=email,phone=phone,aadhar=aadhar,policy=policy,appointment_date=dt,doctor=doctor,coupon=coupon,department=department,message=message,symptoms=str1)
        q.save()
        pdf.cell(200, 10, txt = "",ln = 12, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 13, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 14, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 15, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 20, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 16, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 20, align = 'L')
        pdf.cell(200, 10, txt = "",ln = 20, align = 'L')
        pdf.cell(200, 10, txt = "Thank you for choosing us.",ln = 15, align = 'C')
        pdf.cell(200, 10, txt = "Ritik Vashist",ln = 16, align = 'C')
        pdf.output("GetADoc.pdf")
        dict['Key']="no"
        print("Downloaded Successfully") 
    return render(request,'../templates/index1.html',dict)
