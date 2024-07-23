from django.contrib import admin
from .models import Post, Author, Tag

# to customize admin page for Post
class PostAdmin(admin.ModelAdmin):
    # for slug Django will use slugify inder the hood
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title", "author", "date_created")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
