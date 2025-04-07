from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from catalog.models import category
# Register your models here.


class categoryAdmin(TreeAdmin):
    form = movenodeform_factory(category)

admin.site.register(category,categoryAdmin)