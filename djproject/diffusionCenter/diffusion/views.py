from django.shortcuts import render
from diffusion.models import ContactProfile, Treatment, Material, DiffusionRelation
# Create your views here.
from django.http import HttpResponse
from django.template import loader

use_cdn = False

def index(request):
	return render(request,'main.html', {'use_cdn': use_cdn})

def glossary_search(request, query=''):
	context = {
		'use_cdn': use_cdn,
		'material_list': Material.objects.order_by("short_name"),
		#'relation_list': DiffusionRelation.order_by('diffusion_type').order_by('material_1').order_by('material_2')
	} 
	#print(material_list)
	return render(request, 'glossary.html', context)

def editGlossary(request):
	return HttpResponse("You're editing the glossary with a POST request, right?")

# def integrate (request, terms):
# 	tArray = terms.split('/')[1:]
# 	tupArray = list(map(lambda x: tuple(x.split('-')), tArray))
# 	t2Array = list(map(lambda x: x[0]+"x^"+x[1], tupArray))
# 	print(tupArray)
# 	return HttpResponse("<b>Input Data:</b>  " + ", ".join(tArray) + "<br><b>Parsed Polynomial:</b> " + " + ".join(t2Array))

def setup_profile(request):
	return render(request, 'profile_setup.html', {'use_cdn': use_cdn})

def setup_process(request):
	return render(request, 'process_setup.html', {'use_cdn': use_cdn})

def run_process(request):
	return render(request, 'process_run.html', {'use_cdn': use_cdn})

def saved_results(request):
	return render(request, 'saved_results.html', {'use_cdn': use_cdn})

def add_material (request):
	#if request.method == 'POST':
	#else
	return HttpResponse("hi")

def add_relation (request):
	#if request.method == 'POST':

	#else:
		#form = DiffusionForm
	return HttpResponse("hi")

def add_process(request):
	return HttpResponse("hi")

def add_profile(request):
	return HttpResponse("hi")

def get_result(request):
	return HttpResponse("hi")