from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^glossary/?$', views.glossary_search),
	url(r'^glossary/(?P<query>\w+)/?$', views.glossary_search),
	url(r'^edit/glossary/?$', views.editGlossary),
	#url(r'^integrate(?P<terms>(/[0-9]-[0-9])+)/?$', views.integrate),
	url(r'^setup-profile/?$', views.setup_profile),
	url(r'^setup-process/?$', views.setup_process),
	url(r'^run-process/?$', views.run_process),
	url(r'^saved-results/?$', views.saved_results),
	url(r'^add-material/?$', views.add_material),
	url(r'^add-relation/?$', views.add_relation),
	url(r'^', views.index, name='index')
]