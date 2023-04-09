from django import forms
from tree_menus.models import MenuInstance


class MenuInstanceForm(forms.ModelForm):
    class Meta:
        model = MenuInstance
        fields = ['name', 'init_url', 'final_url', 'parent']

    def del_final_url(self):
        return self.cleaned_data['final_url'] or None

    def del_init_url(self):
        return self.cleaned_data['init_url'] or None
