from django.urls import path
from .views import index
from .views_app.inscrito_views import (
    InscritoListView, InscritoCreateView, InscritoUpdateView, InscritoDeleteView
)
from .views_app.institucion_views import institucion_list, institucion_detail
from .views_app.api_views import autor_info, InscritoAPI, InstitucionAPI  

urlpatterns = [
    path('', index, name='index'), 
    path('inscritos/', InscritoListView.as_view(), name='inscrito_list'),
    path('inscritos/add/', InscritoCreateView.as_view(), name='inscrito_add'),
    path('inscritos/edit/<int:pk>/', InscritoUpdateView.as_view(), name='inscrito_edit'), 
    path('inscritos/delete/<int:pk>/', InscritoDeleteView.as_view(), name='inscrito_delete'), 
    path('instituciones/', institucion_list, name='institucion_list'),
    path('instituciones/<int:id>/', institucion_detail, name='institucion_detail'),
    path('api/autor/', autor_info, name='autor_info'),
    path('api/inscritos/', InscritoAPI.as_view(), name='inscrito_api'),
    path('api/instituciones/', InstitucionAPI.as_view(), name='institucion_api'),  
    
]
