from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar")
    #on_delete User silinirse O User'a ait olan tablolarında silinmesini sağlar.
    #ForeingKey ile var olan tabloya atıfta bulunuyoruz.
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    #auto_now_add = True created_date'ye veri vermiyecez veri eklediğimizde otomatikmen o anki tarihi created_date'e ekler.
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    surname = models.CharField(max_length=100,verbose_name="Soyad")
    email =models.EmailField()
    message=models.TextField()

