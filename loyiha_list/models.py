from django.db import models

class AboutAdmissionWhyUs(models.Model):
    PAGES =(
        ('About', 'About'),
        ('Admission', 'Admission'),
        ('WhyUs', 'WhyUs'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    page = models.CharField(max_length=50, choices=PAGES)
    def __str__(self):
        return f"{self.title} - {self.description}"

class ContactUs(models.Model):
    fullname=models.CharField(max_length=100, verbose_name='F.I.O')
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    

class Social(models.Model):
    facebook=models.CharField(max_length=255,blank=True,null=True)
    twitter=models.CharField(max_length=255,blank=True,null=True)
    linkenid=models.CharField(max_length=255,blank=True,null=True)
    instagram=models.CharField(max_length=255,blank=True,null=True)
