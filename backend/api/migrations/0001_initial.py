# Generated by Django 4.1.3 on 2022-12-03 12:56

import api.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('education', models.JSONField()),
                ('work_place', models.JSONField()),
                ('academic_degree', models.JSONField()),
                ('academic_title', models.JSONField()),
            ],
            options={
                'verbose_name': 'автора',
                'verbose_name_plural': 'Авторы',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'секцию',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('stype', models.TextField(choices=[('None', 'Сотрудник'), ('program_PR', 'Председатель программного комитета'), ('program_Member', 'Член программного комитета'), ('org_PR', 'Председатель организационного комитета'), ('org_Member', 'Член организационного комитета')], default=('None', 'Сотрудник'))),
                ('img', models.ImageField(default='', upload_to='stuff/')),
            ],
            options={
                'verbose_name': 'направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(null=True, upload_to=api.models.user_directory_path)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.author')),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.section')),
            ],
        ),
    ]
