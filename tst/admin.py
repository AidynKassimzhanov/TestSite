from django.contrib import admin
from .models import Profile, Discipline, Tests, Questions, Answers, Stats, TmpTest

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user',)
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# admin.site.register(Book)

admin.site.register(Profile)
admin.site.register(Discipline)

class QuestionsInline(admin.TabularInline):
    model = Questions

class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    inlines = [QuestionsInline]

admin.site.register(Tests, TestAdmin)

class AnswersInline(admin.TabularInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'test')
    inlines = [AnswersInline]

admin.site.register(Questions, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'question')
    
admin.site.register(Answers, AnswerAdmin)

class StatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'result', 'time')

admin.site.register(Stats, StatsAdmin)

class TmpAdmin(admin.ModelAdmin):
    list_display = ('id', 'qid', 'ans', 'ball')
admin.site.register(TmpTest, TmpAdmin)