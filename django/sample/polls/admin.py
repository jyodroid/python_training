from django.contrib import admin
from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently') #Adds more fields to display
    list_filter = ['pub_date'] #adds a filter to to the rigth
    search_fields = ['question_text'] #adds a search bar

admin.site.register(Question, QuestionAdmin)
