from django.db import models
# Create your models here.
from django.dispatch import receiver

from django.db.models.signals import post_save, pre_save, pre_delete, post_delete, m2m_changed
from compte.utils import send_email_with_template

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Plan(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title



class Subcribe(models.Model):

    STATUS = ( 
        ('S', 'Success'),
       ( 'F', 'Failed'),
    )
    email = models.EmailField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.email 



class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    student = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.title

class DeleteStudent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return self.name

from django.conf import settings
@receiver(post_save, sender=Student)
def send_email_to_admin(sender, instance, created, **kwargs):
    if created:
        # send email to admin

        subject = 'New student registered'
        template_name = 'email/new_student.html'

        context = {
            'name': instance.name,
            'email': instance.email,
        }

        to_email = [instance.email]

        from_email = settings.EMAIL_HOST_USER

        send_email_with_template.delay(subject, template_name, context, to_email, from_email)

    else:
        print('Student updated')


@receiver(pre_save, sender=Student)
def send_email_to_student(sender, instance, **kwargs):
  
    # send email to admin

    subject = 'Welcome to our website'
    template_name = 'email/welcome.html'

    context = {
        'name': instance.name,
        'description': instance.email,
    }

    to_email = [instance.email]

    from_email = settings.EMAIL_HOST_USER

    send_email_with_template.delay(subject, template_name, context, to_email, from_email)

   


# pre_save.connect(send_email_to_student, sender=Student)
# pre_save.disconnect(send_email_to_student, sender=Student)


@receiver(post_delete, sender=Student)
def save_delete_student(sender, instance, **kwargs):
    DeleteStudent.objects.create(name=instance.name, email=instance.email)



@receiver(m2m_changed, sender=Course.student.through)    
def send_email_to_student(sender, instance, action, **kwargs):
    print(action)
    if action == 'post_add':
        subject = 'New student registered'
        template_name = 'email/welcome.html'

        context = {
            'name': instance.title,
            'description': instance.description,
        }

        to_email = ["donaldtedom0@gmail.com"]

        from_email = settings.EMAIL_HOST_USER

        send_email_with_template.delay(subject, template_name, context, to_email, from_email)
    elif action == 'post_remove':
        subject = 'Student removed'
        template_name = 'email/welcome.html'

        context = {
            'name': instance.title,
            'description': instance.description,
        }

        to_email = ["donaldtedom0@gmail.com"]

        from_email = settings.EMAIL_HOST_USER

        send_email_with_template.delay(subject, template_name, context, to_email, from_email)                    
    else:
        print('Course updated')