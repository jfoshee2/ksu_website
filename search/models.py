from django.db import models


class Book(models.Model):
    #cover = models.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    description = models.CharField(max_length=999999)
    new_book = models.IntegerField()
    used_book = models.IntegerField()
    rental_book = models.IntegerField()
    ebook = models.IntegerField()
    new_book_price = models.IntegerField()
    used_book_price = models.IntegerField()
    rental_book_price = models.IntegerField()
    ebook_price = models.IntegerField()

    def __str__(self):
            return self.title + ' - ' + self.author

class Course(models.Model):
    #inside of the ForeignKey function it should be (book, on_delete=models.CASCADE)
    book = models.ForeignKey(Book)
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
            return self.course_name + ' - ' + self.profesor

