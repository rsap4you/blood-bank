from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Patient/',null=True,blank=True)

    age=models.PositiveIntegerField()
    bloodgroup=models.CharField(max_length=10,null=False,default=0)
    # disease=models.CharField(max_length=100)
    # doctorname=models.CharField(max_length=50)

    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    Email = models.EmailField(max_length=250,null=False,default=0)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['kumaramarjeetraj7725@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/patient/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
            