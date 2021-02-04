from django.utils.translation import gettext as _
from django.db import models


class Author(models.Model):
    full_name = models.TextField(verbose_name=_("Имя автора"))
    def __str__(self):
        return self.full_name
    birth_year = models.SmallIntegerField(verbose_name=_("Год рожения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

class PublishingHouse(models.Model):
    name = models.TextField(verbose_name=_("Издательство"))
    country = models.CharField(null='-', max_length=2, verbose_name=_("Страна"))
    city = models.TextField(null='-', verbose_name=_("Город"))
    def __str__(self):
        return self.name
11
class Book(models.Model):
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"))
    title = models.TextField(verbose_name=_("Название"))
    def __str__(self):
        return self.title
    description = models.TextField(verbose_name=_("Аннотация"))
    year_release = models.SmallIntegerField(verbose_name=_("Год издания"))
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"))
    price = models.DecimalField(max_digits=12, decimal_places=2,
                                verbose_name=_("Цена"))
    author = models.ForeignKey("p_library.Author", on_delete=models.CASCADE,
                               verbose_name=_("Автор"),
                               related_name="book_author")
    pub_house = models.ForeignKey(PublishingHouse, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
