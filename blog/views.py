from django.shortcuts import render
from datetime import date

#to have data provided from python and not hardcoded 
# we are going to use temp var "posts"
posts = [
  {
    "slug": "payment-gateway",
    "image": "The-Process.jpeg",
    "author": "Ilia",
    "date": date(2024, 6, 5),
    "title": "Payment Gateway",
    "excerpt": "The text about the payment Gatewey. The text about the payment Gatewey. The text about the payment Gatewey.The text about the payment Gatewey.",
    #to create a multi line string - use
    "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    """
  },
  {
    "slug": "ant-farm",
    "image": "The-Ant.jpeg",
    "author": "Ilia",
    "date": date(2024, 6, 5),
    "title": "Ant Farm",
    "excerpt": "The text about the Ant Farm. The text about the Ant Farm. The text about the Ant Farm.The text about the Ant Farm.",
    #to create a multi line string - use
    "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    """
  },
  {
    "slug": "hike-in-the-mountains",
    "image": "The-Process.jpeg",
    "author": "Ilia",
    "date": date(2024, 6, 5),
    "title": "Mountain hiking",
    "excerpt": "The text about the hiking. The text about the payment Gatewey. The text about the payment Gatewey.The text about the payment Gatewey.",
    #to create a multi line string - use
    "content": """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    Lorem ipsum dolor sit amet consectetur adipisicing elit. 
    Quasi accusamus, necessitatibus doloremque voluptas optio expedita numquam ducimus nam error ratione perspiciatis consequuntur praesentium. 
    Assumenda perspiciatis repellat maxime nihil asperiores quas?
    """
  }
]
# Create your views here.

def index(request):
    cards = list(post_text.items())[-3:]
            
    return render(request, "blog/index.html", {
        "cards": cards
          })

def posts(request):
  return render(request, "blog/all-posts.html")

#we are going to use the dynamic url - we have to specify "slug" as a context
def post_detail(request, slug):
  return render(request, "blog/post-detail.html")
