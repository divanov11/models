from django.db import models


#https://docs.djangoproject.com/en/2.1/topics/db/models/
class Piece(models.Model):
	test = models.CharField(max_length=200, blank=True,  null=True)

class Article(Piece):
	article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
	test1 = models.CharField(max_length=200 , blank=True,  null=True)


class Book(Piece):
	book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)
	test2 = models.CharField(max_length=200, blank=True,  null=True)


class BookReview(Book, Article):
	test3 = models.CharField(max_length=200, blank=True,  null=True)
