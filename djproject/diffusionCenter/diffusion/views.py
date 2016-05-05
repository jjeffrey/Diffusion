from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world, you're at the diffusion center!")

def glossarySearch(request, query):
		message = 'You submitted: ' + query
		return HttpResponse(message)

def editGlossary(request):
	return HttpResponse("You're editing the glossary with a POST request, right?");
# def setTrial(request, query="diffusion"):

def integrate (request, terms):
	tArray = terms.split('/')[1:]
	tupArray = list(map(lambda x: tuple(x.split('-')), tArray))
	t2Array = list(map(lambda x: x[0]+"x^"+x[1], tupArray))
	print(tupArray)
	return HttpResponse("<b>Input Data:</b>  " + ", ".join(tArray) + "<br><b>Parsed Polynomial:</b> " + " + ".join(t2Array))