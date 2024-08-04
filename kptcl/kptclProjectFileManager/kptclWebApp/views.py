from django.shortcuts import render

# Create your views here.
def response(request):
    return render(request, "Contractor_dash.html", None)