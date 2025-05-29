from django.db import models

# Create your models here.

class Cover(models.Model):
    imag_default = models.ImageField(upload_to='logos/', blank=True)

    title1 = models.CharField(max_length=50, blank=True)

    title2 = models.CharField(max_length=50, blank=True)

    title3 = models.CharField(max_length=50, blank=True)

    logo = models.ImageField(upload_to='logos/', blank=True)
    width = models.PositiveIntegerField(default=150, blank=True)
    height = models.PositiveIntegerField(default=40, blank=True)

    carousel_image_1 = models.ImageField(upload_to='carousel/', blank=True)
    carousel_image_1_title = models.CharField(max_length=50, blank=True)
    carousel_image_1_text = models.CharField(max_length=300, blank=True)


    carousel_image_2 = models.ImageField(upload_to='carousel/', blank=True)
    carousel_image_2_title = models.CharField(max_length=50, blank=True)
    carousel_image_2_text = models.CharField(max_length=300, blank=True)

    carousel_image_3 = models.ImageField(upload_to='carousel/', blank=True)
    carousel_image_3_title = models.CharField(max_length=50, blank=True)
    carousel_image_3_text = models.CharField(max_length=300, blank=True)
    carousel_3_boton = models.CharField(max_length=15, blank=True)

    tarjeta_1_imagen = models.ImageField(upload_to='card/', blank=True)
    text1 = models.CharField(max_length=300, blank=True)

    tarjeta_2_imagen = models.ImageField(upload_to='card/', blank=True)
    text2 = models.CharField(max_length=300, blank=True)

    tarjeta_3_imagen = models.ImageField(upload_to='card/', blank=True)
    text3 = models.CharField(max_length=300, blank=True)

    presentation1_text_primary = models.CharField(max_length=300, blank=True)
    presentation1_text_secundary = models.CharField(max_length=300, blank=True)
    presentation1_text = models.CharField(max_length=300, blank=True)
    presentation1_image = models.ImageField(upload_to='presentation/', blank=True)

    presentation2_text_primary = models.CharField(max_length=300, blank=True)
    presentation2_text_secundary = models.CharField(max_length=300, blank=True)
    presentation2_text = models.CharField(max_length=300, blank=True)
    presentation2_image = models.ImageField(upload_to='presentation/', blank=True)

    presentation3_text_primary = models.CharField(max_length=300, blank=True)
    presentation3_text_secundary = models.CharField(max_length=300, blank=True)
    presentation3_text = models.CharField(max_length=300, blank=True)
    presentation3_image = models.ImageField(upload_to='presentation/', blank=True)
    
    class Meta:
        verbose_name_plural = 'Covers'

    def __str__(self):
        return "Cover"