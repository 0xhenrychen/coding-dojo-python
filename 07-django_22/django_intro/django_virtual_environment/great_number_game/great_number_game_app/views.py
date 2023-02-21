from django.shortcuts import render, redirect
import random

def index(request):
    if "random_number" not in request.session:
        request.session["random_number"] = random.randint(1, 100)
        request.session["message"] = ""
    return render(request, "index.html")

def guess(request):
    request.session["guess_number"] = int(request.POST["number_guess"])
    print("Random number is:", request.session["random_number"])
    request.session["message"] = ""
    print("Your guess is:", request.session["guess_number"])
    
    
    if request.session["guess_number"] > request.session["random_number"]:
        print("Guess number is HIGHER than random number.")
        request.session["message"] = f'Too high!'
    elif request.session["guess_number"] < request.session["random_number"]:
        print("Guess number is LOWER than random number.")
        request.session["message"] = f'Too low!'
    else:
        print("Guess number is EQUAL to random number.")
        request.session["message"] = f'{request.session["random_number"]} was the number!'
    return redirect("/")

def reset(request):
    del request.session["random_number"]
    # del request.session["guess_number"]
    # del request.session["message"]
    return redirect("/")


# def index(request):
#     if "counter" in request.session:
#         print("Key exists!")
#         request.session["counter"] += 1
#         print("Value of counter is:", request.session["counter"])
#     else:
#         print("Key counter does NOT exist")
#         request.session["counter"] = 0
        
#         request.session["counter"] += 1
#         print("Value of counter is:", request.session["counter"])
#     return render(request, "index.html")

# def counter2(request):
#     if "counter" in request.session:
#         print("Key exists!")
#         request.session["counter"] += 2
#         print("Value of counter is:", request.session["counter"])
#     else:
#         print("Key counter does NOT exist")
#         request.session["counter"] = 0
        
#         request.session["counter"] += 2
#         print("Value of counter is:", request.session["counter"])
#     return redirect("/")



