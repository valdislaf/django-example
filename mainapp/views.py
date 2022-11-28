from django.shortcuts import render

def index(request):
     return render(request,'mainapp/index.html')
     
def contact(request):
     return render(request,'mainapp/basic.html', {'values':['bla-bla-bla','1687343(0990)']})
     
def news(request):
     return render(request,'mainapp/news1.html')
     
def symbols(request):
     return render(request,'mainapp/symbols.html')


# Create your views here.
