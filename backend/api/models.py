from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
stuff_type = (
    ("None", "Сотрудник"),
    ("program_PR", "Председатель программного комитета"),
    ("program_Member", "Член программного комитета"),
    ("org_PR", "Председатель организационного комитета"),
    ("org_Member", "Член организационного комитета"),
)

def user_directory_path(instance, filename):
    return 'files/users/{0}/{1}'.format(instance.owner.name, filename)

class Worker(models.Model):
    name = models.CharField(max_length=255, default="")
    desc = models.TextField(blank=True)
    stype = models.TextField(choices=stuff_type, default=stuff_type[0])
    img = models.ImageField(upload_to="img/workers/", default="")

    def __str__(self):
        return f'{self.name}: {self.stype}'

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'Сотрудники'

# class dschool(models.Model):
#     name = models.CharField(max_length=50, blank=True)

    # class Meta:
    #     verbose_name = 'направление'
    #     verbose_name_plural = 'Направления'

class Section(models.Model):
    name = models.CharField(max_length=255, blank=True)
    # school = models.ForeignKey(dschool, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'секцию'
        verbose_name_plural = 'Секции'

class Author(User):
    # last_name = models.CharField(max_length= 50)
    education = models.JSONField()
    work_place = models.JSONField()
    academic_degree = models.JSONField()
    academic_title = models.JSONField()

    class Meta:
        verbose_name = "автора"
        verbose_name_plural = "Авторы"

class Reviewer(User):
    pass


class File(models.Model):
    name = models.FileField(upload_to=user_directory_path, null=True)
    owner = models.ForeignKey(Author, on_delete=models.CASCADE, default="")
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, blank=True)

    def delete(self, *args, **kwargs):
        # До удаления записи получаем необходимую информацию
        storage, path = self.name.storage, self.name.path
        # Удаляем сначала модель ( объект )
        super(File, self).delete(*args, **kwargs)
        # Потом удаляем сам файл
        storage.delete(path)

    def __str__(self):
        return self.name.path