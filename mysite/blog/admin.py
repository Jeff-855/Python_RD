from django.contrib import admin
from .models import Post
from .models import Test

admin.site.register(Post)
admin.site.register(Test)