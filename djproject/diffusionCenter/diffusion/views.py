from django.shortcuts import render
from diffusion.models import ContactProfile, Treatment, Material, DiffusionRelation
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
	material_list = Material.objects.order_by("short_name")
	short_name_list = [material.short_name for material in material_list]
	context = {
		'short_name_list': short_name_list,
	} 
	print(material_list)
	template = loader.get_template('main.html')
	return HttpResponse(template.render(context, request))

def glossarySearch(request, query):
	context = {
		'material_list': Material.objects.order_by("short_name"),
		#'relation_list': DiffusionRelation.order_by('diffusion_type').order_by('material_1').order_by('material_2')
	} 
	print(material_list)
	template = loader.get_template('diffusion/templates/glossary.html')
	return HttpResponse(template.render(context, request))

def editGlossary(request):
	return HttpResponse("You're editing the glossary with a POST request, right?")
# def setTrial(request, query="diffusion"):

def integrate (request, terms):
	tArray = terms.split('/')[1:]
	tupArray = list(map(lambda x: tuple(x.split('-')), tArray))
	t2Array = list(map(lambda x: x[0]+"x^"+x[1], tupArray))
	print(tupArray)
	return HttpResponse("<b>Input Data:</b>  " + ", ".join(tArray) + "<br><b>Parsed Polynomial:</b> " + " + ".join(t2Array))