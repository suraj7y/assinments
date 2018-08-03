from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^', views.PersonListView.as_view(), name='person_changelist'),
    url(r'^add/', views.PersonCreateView.as_view(), name='person_add'),
    url(r'^<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    url(r'^ajax/load-cities/$', views.load_cities, name='ajax_load_cities'),

]