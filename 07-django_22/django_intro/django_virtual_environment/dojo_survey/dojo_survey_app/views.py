from django.shortcuts import render
    
def index(request):
    return render(request, "index.html")

def dojo_form(request):
    context = {
        "name": request.POST["name"],
        "location": request.POST["dojo_location"],
        "language": request.POST["language"],
        "comment": request.POST["comment"],
    }
    return render(request, "result.html", context)