from django.db import models

# Create your models here.
class CreateModel(models.Model):
    column_name = models.CharField(max_length=50)
    column_type = models.CharField(
        max_length=20,
        blank=False,
    )
    generate_type = models.CharField(
        max_length=20,
        blank=False,
    )
    link_column_name = models.CharField(max_length=50)
    data_type = models.CharField(
        max_length=20,
        blank = False,
    )

    ##### normal column #####
    text = models.TextField()
    number_min = models.FloatField()
    number_max = models.FloatField()
    number_step = models.FloatField()
    date_min = models.DateField()
    date_max = models.DateField()
    date_step = models.IntegerField()
    datetime_min = models.DateTimeField()
    datetime_max = models.DateTimeField()
    datetime_step = models.IntegerField()

    ##### link column #####
    link_text = models.TextField()
    link_number_min = models.FloatField()
    link_number_max = models.FloatField()
    link_number_step = models.FloatField()
    link_date_min = models.IntegerField()
    link_date_max = models.IntegerField()
    link_datetime_min = models.IntegerField()
    link_datetime_max = models.IntegerField()
    