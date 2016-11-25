from django.db import models


class Book(models.Model):
    cover = models.CharField(max_length=10000, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    description = models.CharField(max_length=999999)
    new_book_quantity = models.FloatField()
    used_book_quantity = models.FloatField()
    rental_book_quantity = models.FloatField()
    ebook_quantity = models.FloatField()
    new_book_price = models.FloatField()
    used_book_price = models.FloatField()
    rental_book_price = models.FloatField()
    ebook_price = models.FloatField()
    in_cart = models.BooleanField(default=False)

    def __str__(self):
            return self.title + ' - ' + self.author


class Course(models.Model):
    # inside of the ForeignKey function it should be (book, on_delete=models.CASCADE)
    book = models.ForeignKey(Book)
    course_number = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
            return self.course_name + ' - ' + self.profesor

