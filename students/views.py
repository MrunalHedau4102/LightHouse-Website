from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from students.forms import StudentsForm
from students.models import Students
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == "POST":
        
        form = StudentsForm(request.POST)
        
        if form.is_valid():
            try:
                
                form.save()
                # messages.success(request, 'You have successfully subscribed!!!')
                #send mail
                # send_mail(
                #     'ty,django test mail',#subject
                #     'message,testing sucessful!',#messgae
                #     'swastikdubey123@gmail.com',#from email
                #     ['tebej73103@nubenews.com'],#to email
                #     fail_silently=False
                # )
              
                messages.success(request, 'Your message has been sent!')
                return render(request,'index.html')  
                # return redirect('/')
                
                
            except:
                pass
    
    else:
        form= StudentsForm() 
    return render(request,'index.html')   

def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')
def contact(request):
        if request.method == "POST":
        
            name = request.POST.get('name')
            email = request.POST.get('email')
            describe = request.POST.get('describe')
            


            
            try:
                    msg= "from:-"+"\n name :" + name + "\n email :" + email + "\n describe : "+describe
                    subject = 'Your Order Confirmation Details!!!'
                    message1 = msg
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [""]#write reciever mail id here
                    send_mail( subject, message1, email_from, recipient_list )
                    print(message1)
                    msg="Order Booked Successfully !!! \n Message and Email Sent to the Company/Party !!!"
                    return render(request,'contact.html')
            except:
                    pass  
        else:
        
            return render(request,'contact.html')           
def technical_about(request):
    return render(request,'technical_about.html')
def editors_about(request):
    return render(request,'editors_about.html')
def design_about(request):
    return render(request,'design_about.html')
def departmenthead_about(request):
    return render(request,'departmenthead_about.html')
def CMA_about(request):
    return render(request,'CMA_about.html')
            
        