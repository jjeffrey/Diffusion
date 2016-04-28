from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^glossary/(?P<query>\w+)/', views.glossarySearch),
	url(r'^edit/glossary/', views.editGlossary),
	url(r'^integrate/(?P<terms>([0-9]-[0-9]/)+)', views.integrate),
	url(r'^', views.index, name='index')
]