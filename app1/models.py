from django.db import models

# Create your models here.


class Event(models.Model):

    head = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    photo = models.ImageField(blank=True, upload_to='images', help_text='150x150px', verbose_name='Ссылка на фот')
    descript = models.TextField(help_text="Введите описание")
    author = models.CharField(max_length=100)
    date_in = models.DateTimeField(null=True, blank=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        ordering = ["-date_in"]
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
#        return self.head
        return 'id={0} Заголовок={1}'.format (self.id, self.head)