from django.shortcuts import render

def master_table(request):
    return render(request, 'map/index.html')
