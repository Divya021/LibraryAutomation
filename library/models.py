from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    bookid=models.IntegerField(null=True)
    title=models.CharField(max_length=100,null=True)
    Authorname=models.CharField(max_length=50,null=True)
    cost=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)

    def  __str__(self):
        return self.title
class Studentinfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    studentid=models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name

class Placeorder(models.Model):
    user=models.ForeignKey(Studentinfo,on_delete=models.CASCADE,null=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    issuedate = models.DateField(null=True)
    expirydate = models.DateField(null=True)

    def __str__(self):
        return self.user.user.username+" "+self.book.title+" "+self.book.Authorname
