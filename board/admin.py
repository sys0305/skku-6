from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):  
  fields = ["title", "nickname", "content"]
  list_display = ["id", "title", "nickname"]
  pass

# admin.site.register(<model>, <Admin_class>)
admin.site.register(Board, BoardAdmin)
