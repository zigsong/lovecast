# Generated by Django 2.2.3 on 2019-08-11 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedpage', '0014_profile_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.FeedComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feedcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedpage.FeedComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedcomment',
            name='comment_disliked_users',
            field=models.ManyToManyField(blank=True, related_name='comments_disliked', through='feedpage.CommentDislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedcomment',
            name='comment_liked_users',
            field=models.ManyToManyField(blank=True, related_name='comments_liked', through='feedpage.CommentLike', to=settings.AUTH_USER_MODEL),
        ),
    ]