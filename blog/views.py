from django.shortcuts import render

post_text = {"Ants":"Text about ants", "Payments":"Text about payments", "Hiking":"Text about hiking", "Baking":"Text "}
# Create your views here.

def index(request):
    cards = list(post_text.items())[-3:]
            
    return render(request, "blog/index.html", {
        "cards": cards
          })

def posts(request):
  pass 

def post_detail(request):
  pass
