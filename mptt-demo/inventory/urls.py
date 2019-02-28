from django.conf.urls import include, url
from . import  views

urlpatterns = [
                url(r'^get_tree_ajax/', views.get_tree_ajax ,name='get_tree_ajax'),
                url(r'^move_node_ajax/', views.move_node_ajax ,name='move_node_ajax'),
                url(r'^insert_node_ajax/', views.insert_node_ajax ,name='insert_node_ajax'),
                url(r'^delete_node_ajax/', views.delete_node_ajax ,name='delete_node_ajax'),
                 ]
               
               