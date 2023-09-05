# Generated by Django 4.1.6 on 2023-02-17 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0005_author_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_outlet.author'),
        ),
    ]
