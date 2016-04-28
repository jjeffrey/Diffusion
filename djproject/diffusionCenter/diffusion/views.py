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
	tArray = terms.split('/')
	tupArray = map(lambda x: tuple(x.split('-')), tArray)
	return HttpResponse(", ".join(tArray))