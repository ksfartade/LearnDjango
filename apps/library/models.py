from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    authors = models.ManyToManyField('Author', related_name='books', null=True, blank=True)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class Education(models.Model):
    institute = models.CharField(max_length=100, null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    institute = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True)

