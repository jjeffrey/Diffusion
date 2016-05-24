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
	url(r'^', views.index, name='index')
]