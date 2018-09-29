from django.contrib import admin

from .models import *

admin.site.register(Piece)
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(BookReview)