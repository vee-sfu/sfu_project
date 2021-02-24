from django.db import models
from django.urls import reverse
# Create your models here.


class Event(models.Model):

    head = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    photo = models.ImageField(blank=True, upload_to='images', help_text='150x150px', verbose_name='Ссылка на фот')
    descript = models.TextField(help_text="Введите описание")
    author = models.CharField(max_length=100)
    date_in = models.DateTimeField(null=True, blank=True)


    @property
    def main_text(self):
        for i in range(200, 230):
          if self.descript[i:i+1] == ' ':
            break
        return self.descript[:i]+' ...'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        ordering = ["-date_in"]
    

# обязательный метод - используется для представления отдельных записей на сайте администрирования
# (и в любом другом месте, где вам нужно обратиться к экземпляру модели)
    def __str__(self):  
        """
        String for representing the Model object (in Admin site etc.)
        """
#        return self.head
        return 'id={0} Заголовок={1}'.format (self.id, self.head)


# возвращает URL-адрес для отображения отдельных записей модели на веб-сайте 
# (при этом Django автоматически добавит кнопку «Просмотр на сайте» 
# на экранах редактирования записей модели на сайте администратора)
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('event', args=[str(self.id)])





















