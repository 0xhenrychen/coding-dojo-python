from django.shortcuts import render, redirect
    
def index(request):
    if "counter" in request.session:
        print("Key exists!")
        request.session["counter"] += 1
        print("Value of counter is:", request.session["counter"])
    else:
        print("Key counter does NOT exist")
        request.session["counter"] = 0
        
        request.session["counter"] += 1
        print("Value of counter is:", request.session["counter"])
    return render(request, "index.html")

def counter2(request):
    if "counter" in request.session:
        print("Key exists!")
        request.session["counter"] += 2
        print("Value of counter is:", request.session["counter"])
    else:
        print("Key counter does NOT exist")
        request.session["counter"] = 0
        
        request.session["counter"] += 2
        print("Value of counter is:", request.session["counter"])
    return render(request, "index.html")

def destroy(request):
    del request.session["counter"]
    return redirect("/")

