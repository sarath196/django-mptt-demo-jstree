from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django_ajax.decorators import ajax
import json

from inventory.models import Category
# Create your views here.

class CategoryTreeView(TemplateView):
    template_name = 'inventory/category_list.html'  

# get all tree nodes 
@ajax
def get_tree_ajax(request):
    #import ipdb;ipdb.set_trace();
    tree_set = Category._tree_manager.values()
    data = []
    for i in tree_set:
        if not i['parent_id']:
            parent_id = '#'
        else:
            parent_id = 'j1_'+str(i['parent_id'])
        data.append(
            { "id" : 'j1_'+str(i['id']), "parent" : parent_id, "text" : i['name'] }
            )
        
    
    return HttpResponse(json.dumps(data), content_type="application/json")

# move tree node
@ajax
def move_node_ajax(request):
    node_id = request.POST['node_id']
    parent_id = request.POST['parent_id']
    
    try:
        node_set = Category.objects.get(id= int(node_id.split("_")[1]))
        parent_set = Category.objects.get(id = int(parent_id.split("_")[1]))
    
        category = Category()
        category._tree_manager.move_node(node_set, parent_set)
    except:
        return False
    return True

# insert new tree nodes
@ajax
def insert_node_ajax(request):
    node_id = request.POST['node_id']
    parent_id = request.POST['parent_id']
    node_text = request.POST['node_text']
    new_node_id = ''
         
    try:
        node_set = Category.objects.get(id= int(node_id.split("_")[1]))
        parent_set = Category.objects.get(id = int(parent_id.split("_")[1]))
        node_set.name = node_text
        node_set.parent = parent_set
        node_set.save()
    except:
        parent_set = Category.objects.get(id = int(parent_id.split("_")[1])) 
        new_node = Category.objects.create(name=node_text, parent = parent_set)
        new_node.save()
        new_node_id = 'j1_'+str(new_node.id)
          
    return new_node_id
    
# delet tree node        
@ajax
def delete_node_ajax(request):
    node_id = request.POST['node_id']
    parent_id = request.POST['parent_id']
    
    try:
        node_set = Category.objects.get(id= int(node_id.split("_")[1])).delete()
    except:
        return False
    return True 