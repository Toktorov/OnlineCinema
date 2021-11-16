from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    country = models.CharField(max_length=100, verbose_name='Страна')
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title}, {self.year}"

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ('-created', )

class FilmImage(models.Model):
    film = models.ForeignKey(Film, 
        on_delete=models.CASCADE, 
        related_name='film_image'
    )

    image = models.ImageField(
        upload_to = 'film', 
        verbose_name='Фотография фильма'
    )

    class Meta:
        verbose_name = 'Фото фильма'
        verbose_name_plural = 'Фотографии фильма'