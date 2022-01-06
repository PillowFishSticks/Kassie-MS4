# Imports
# 3rd party:
from django.urls import path

# Internal:
from . import views


urlpatterns = [
    path('', views.inspo_items, name='inspo_items'),
    path('add_inspo_item/', views.add_inspo_item, name='add_inspo_item'),
    path('manage_inspo_items/', views.manage_inspo_items,
         name='manage_inspo_items'),
    path('edit_inspo_item/<int:inspo_item_id>/', views.edit_inspo_item,
         name='edit_inspo_item'),
    path('delete_inspo_item/<int:inspo_item_id>/', views.delete_inspo_item,
         name='delete_inspo_item'),
    path('<int:inspo_item_id>/', views.inspo_item, name='inspo_item'),
]
