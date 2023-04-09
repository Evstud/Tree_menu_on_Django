from django import template
from django.shortcuts import get_object_or_404
from tree_menus.models import MenuInstance


register = template.Library()


@register.inclusion_tag('main_html.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(MenuInstance, name=menu_name, parent=None)
    local_context = {'menu_instance': menu}
    requested_url = context['request'].path

    try:
        active_menu_instance = MenuInstance.objects.get(final_url=requested_url)
    except:
        pass
    else:
        children_ids = active_menu_instance.get_children_ids() + [active_menu_instance.id]
        local_context['children_ids'] = children_ids
    return local_context


@register.inclusion_tag('main_html.html', takes_context=True)
def draw_children(context, menu_instance_id):
    menu_instance = get_object_or_404(context, menu_instance_id)
    local_context = {'menu_instance': menu_instance}
    if 'children_ids' in context:
        local_context['children_ids'] = context['children_ids']
    print(context)
    return local_context
