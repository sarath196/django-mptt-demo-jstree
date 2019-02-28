from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


from .models import Category

# Register your models here.
class CategoryAdmin(MPTTModelAdmin):
    fields = ['name', 'description', 'parent']
    list_display = ('name', )

    mptt_level_indent = 15
    #change_list_template = 'demo_mptt/category_list.html'


admin.site.register(Category, DraggableMPTTAdmin)



