from django.db import models
#from django.utils.text import slugify
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    # lets use the special Email field since it has a email validator 
    # it is also possuble to customise regex pattern 
    e_mail = models.EmailField(null=True)
    
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    # on_delete = models.CASCADE was deleted since we do not want to delete all author's posts in case of author deletion 
    author= models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null = True)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    # set the date when the post was first created
    # it doesn't change it on subsequent saves 
    date_created = models.DateField(auto_now_add=True)
    # with auto_now = True the value will be updated every time the post is edited
    date_edited = models.DateField(auto_now=True)
    # if db_index = True - the db index will be created for this field
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)
    # lets try the TextField - without max_length
    # lets add the MinLengthValidator
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)
    
    # we are going to use admin console to enter data. 
    # we do not need to rewrite the save() method
    
    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
        # super().save(*args, **kwargs) - to call parent class save(). 
        # according to Stackoverflow - it is possible do not use args but I used just in case
    #    super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"Author: {self.author}, {self.title}, {self.date_created}"
        
