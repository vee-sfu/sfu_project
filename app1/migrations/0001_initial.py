# Generated by Django 3.1.5 on 2021-01-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
                ('photo', models.ImageField(blank=True, help_text='150x150px', upload_to='images', verbose_name='Ссылка на фот')),
                ('descript', models.TextField(help_text='Введите описание', max_length=1000)),
                ('author', models.CharField(max_length=100)),
                ('date_in', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-date_in'],
            },
        ),
    ]
