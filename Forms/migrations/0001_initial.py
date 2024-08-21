# Generated by Django 3.2.25 on 2024-07-27 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_type', models.CharField(choices=[('survey', 'Survey'), ('quiz', 'Quiz'), ('poll', 'Poll')], max_length=20)),
                ('description', models.TextField()),
                ('is_private', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('view_counts', models.PositiveIntegerField(default=0)),
                ('user_answer_counts', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
