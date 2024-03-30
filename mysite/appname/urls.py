

from django.urls import path
from . import views
# from .views import add_task, delete_task, edit_task

urlpatterns = [
    path('', views.page_for_ghost, name='ghost_page'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('choise_format', views.choise_format, name='choise_format'),
    path('change_to_word', views.change_to_word, name='change_to_word'),
    path('change_to_pdf', views.change_to_pdf, name='change_to_pdf'),
    path('view_pdf_file', views.view_pdf_file, name='view_pdf_file')
]