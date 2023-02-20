from django.shortcuts import render_to_response, render
from time import gmtime, strftime

def index(request):
    context = {
        "time1": strftime("%a %b %d, %Y", gmtime()),
        "time2": strftime("%I:%M %p", gmtime())
    }
    return render(request, "index.html", context)

