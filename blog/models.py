from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import array

STATUS = (
    (0, "Draft"),
    (1,"Publish")
)

CATEGORIES = (
    (0, "None"),
    (1, "Meme"),
    (2, "Propaganda"),
    (3, "Engineering"),
    (4, "Programming"),
)

class Post (models.Model):
    title = models.CharField(max_length=200, unique=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="media/images/")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    #content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.IntegerField(choices=CATEGORIES, default=0)
    hidden = models.BooleanField(default=False, null=False)
    show_comments = models.BooleanField(default=True, null=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    def info(self):
        print(self.description)
        return self.description
