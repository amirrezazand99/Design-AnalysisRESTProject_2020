from django.db import models
from books.models import Books
from Users.models import user




class Comment(models.Model):
    Addressed_Book = models.ForeignKey(Books,unique = False, null=True, on_delete=models.CASCADE)
    Comment_Author = models.ForeignKey(user,unique = False, on_delete=models.CASCADE)
    Comment_Text = models.TextField(default='نظر کاربر')

    #Owners_HR = models.CharField(max_length=8,choices=[('0','bad'),('1','medium'),('2','good'),('n/a','N/A')],default=('n/a'))        #Owner`s Honesty Rating

    def __str__(self):
        return '"' + str(self.Comment_Author)+ '"' + '`s Comment On ' + '<<' + str(self.Addressed_Book) + ">>"
