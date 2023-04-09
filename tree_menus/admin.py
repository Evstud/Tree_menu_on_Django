from django.contrib import admin
from tree_menus.forms import MenuInstanceForm
from tree_menus.models import MenuInstance


class MenuInst(admin.StackedInline):
    model = MenuInstance
    form = MenuInstanceForm


class MenuInstAdmin(admin.ModelAdmin):
    menus_inst = [MenuInst]
    form = MenuInstanceForm


admin.site.register(MenuInstance, MenuInstAdmin)
