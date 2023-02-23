from django.shortcuts import render
from . models import AboutAdmissionWhyUs,Social
def index_page(request):
    context={
        'link':get_social_link()
    }
    return render (request,'index.html',context)


def get_social_link():
    return Social.objects.first()



def about_page(request):
    about=AboutAdmissionWhyUs.objects.filter().first()
    context={
        'about':about,
        'link':get_social_link()
    }
    return render (request,'about.html',context)


def contact_page(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        AboutAdmissionWhyUs.objects.create(
            fullname=fullname,
            email=email,
            phone=phone,
            subject=subject,
        )
    context={
        'link':get_social_link()
    }
    return render (request,'contact.html',context)
    
def admission_page(request):
    admission=AboutAdmissionWhyUs.objects.filter().first()
    context={
        'admission':admission,
        'link':get_social_link()
    }
    return render (request,'admission.html',context)

def why_us_page(request):
    whyUs=AboutAdmissionWhyUs.objects.filter().first()
    context={
        'whyUs':whyUs,
        'link':get_social_link()
    }
    return render (request,'why.html',context)