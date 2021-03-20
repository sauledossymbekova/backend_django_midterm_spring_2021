from django.db import models
from django.contrib.auth import get_user_model

from midterm.constants import TYPES, BULLET_TYPE

User = get_user_model()


class BookJournalBase(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=100)


class Journal(BookJournalBase):
    type = models.IntegerField(choices=TYPES, default=BULLET_TYPE)
    publisher = models.CharField(max_length=100)