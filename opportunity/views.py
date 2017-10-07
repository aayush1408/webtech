from django.shortcuts import render
# Create your views here.


def add(request):
    if(request.method == 'POST'):
        """to be added"""
    else:
        return(render(request, 'opportunity/add.html', {}))
