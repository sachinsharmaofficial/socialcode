# Generated by Django 4.1.2 on 2022-12-13 06:21

import Ask_Chat_Get.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ask_Chat_Get', '0002_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=Ask_Chat_Get.models.user_ask_path, verbose_name='question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='get',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=Ask_Chat_Get.models.user_get_path, verbose_name='ans'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CHAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to=Ask_Chat_Get.models.user_get_path, verbose_name='comment')),
                ('get', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get', to='Ask_Chat_Get.get')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
