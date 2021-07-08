from django.urls import path
from phones.views import create_entry, show_add_entry, find_entry, show_search_entry, CreatePDF

app_name = 'phones'
urlpatterns = [
    path('create/', create_entry, name='create'),
    path('find/', find_entry, name='find'),
    path('search/',show_search_entry,name='search'),
    path('', show_add_entry, name='show_add_entry_form'),
    path('pdf/',CreatePDF.as_view(),name='create_pdf')
]
