from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    # reformats label shown once object is created
    def __str__(self):
        display_name = '{0.campus_name}'
        return display_name.format(self)

    # displays model as University Campus in browser
    class Meta:
        verbose_name_plural = "University Campus"
