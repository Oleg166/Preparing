from django.db import models


class Good_Item(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255)

    admission_date = models.DateField(verbose_name='Дата поступления',
                                      auto_created=True,
                                      auto_now_add=True)

    price = models.PositiveIntegerField(verbose_name='Цена',
                                        default=0)

    unit = models.CharField(verbose_name='Единица измерения',
                             max_length=255)

    vendor = models.CharField(verbose_name='Поставщик',
                              max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name='Карточка товара'
        verbose_name_plural='Карточки товара'