from email.policy import default
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Представляет собой таблицу с учетными записями администраторов и преподавателей.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    session = models.CharField(max_length=32)
    user_ip = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=200)
    user_priv = models.CharField(max_length=20)
    online_time = models.CharField(max_length=11)

    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user)

# Представляет собой таблицу с предметами и их описанием.
class Discipline(models.Model):
    name = models.CharField(max_length=200, help_text="Название предмета")
    desc = models.TextField(max_length=1000, help_text="Описание предмета")

    def __str__(self):
        return self.name


# Представляет таблицу тестами, их описанием, а также именем автора теста.
class Tests(models.Model):
    name = models.CharField(max_length=50, help_text="Название теста")
    desc = models.TextField(max_length=1000, help_text="Описание теста")
    
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('test-details', args=[str(self.id)])



# Таблица с вопросами, содержит идентификатор теста, к которому принадлежит, вопрос, правильные ответы.
class Questions(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.SET_NULL, null=True)

    question = models.CharField(max_length=200, help_text="Название вопроса")
    right_answer = models.CharField(max_length=1)
    # number = models.IntegerField()

    def __str__(self):
        return self.question


# Таблица с ответами на вопросы.
class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    ball = models.IntegerField()

    def __str__(self):
        return self.name

# Представляет таблицу статистики, в которую собираются данные результатов тестов после их прохождения учащимися.
class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(Tests, on_delete=models.SET_NULL, null=True)
    
    result = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True, verbose_name = 'create time')


# Специальная таблица, которую использует генератор тестов, чтобы сохранить промежуточную информацию
class Tmp(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    
    answers = models.TextField(max_length=1000)
    count = models.IntegerField()
    time = models.DateTimeField(auto_now_add = True, verbose_name = 'create time')

class TmpTest(models.Model):
    qid = models.IntegerField()
    ball = models.IntegerField(default=0)
    ans = models.BooleanField(default=False)