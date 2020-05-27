from django.contrib import admin
from core.models import Polo,Terminal
# Register your models here.

class PoloAdmin (admin.ModelAdmin):
    list_display = ('nomePolo', 'qtdEstoque')

class TerminalAdmin (admin.ModelAdmin):
    list_display = ('id','serialTerminal', 'status','idPoloT')

admin.site.register(Polo, PoloAdmin)