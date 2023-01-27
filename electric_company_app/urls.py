from django.urls import path
from . import views

app_name = 'electric_company_app'

urlpatterns = [
    # path('home/', views.home, name='home'),
    path('oferta/', views.oferta, name='oferta'),
    path('', views.post_list, name='post'),
    path('new/', views.new_post, name='new'),
    path('edit/<int:id>/', views.edit_post, name='edit'),

]
