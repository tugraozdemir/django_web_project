from django.contrib import admin
from .models import Article, Contact
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    #Admin panelde görünecek bilgileri yazıdğımız yer
    list_display_links = ["title","created_date"]
    #üstüne basıldığında içeriğe yönlendirmesini sağlayan kod
    search_fields = ["title"]
    #arama çubuğu ekler
    list_filter = ["created_date"]
    #created_Date eklediğimizde süzme paneli açılır (son 7 gün,bugün  vb)
    class Meta:
        model = Article
        #class meta django için özel bir classdır ArticleAdmin clasının
        #article'den türediğini bildiririz.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin,):
    list_display=('name','surname','email',)
    
    

