from django.shortcuts import render
from datetime import date
from .models import Post

#to have data provided from python and not hardcoded 
# we are going to use temp var "posts"
'''
all_posts = [
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
  },
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
  }
]
'''
# Create your views here.

#def get_date(post):
#  return post['date']

def index(request):
    # queue to get sorted list of objects according to the "-date_created" + "-id"
    sorted_posts = Post.objects.all().order_by("-id")
    latest_posts = sorted_posts[:3]
            
    return render(request, "blog/index.html", {
        "latest_posts": latest_posts
          })
    
#I had a slug for this view but I do not hav <slug:slug> for this url as a dynamic segment
def posts(request):
  all_posts = Post.objects.all()
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

#we are going to use the dynamic url - we have to specify "slug" as a context
def post_detail(request, slug):
  all_posts = Post.objects.all()
  selected_post=next(post for post in all_posts if post.slug==slug)
  return render(request, "blog/post-detail.html",{
    #the context mut be with the same name as 
    "post": selected_post
  })
