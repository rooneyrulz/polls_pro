from django.contrib import admin

# from choice.models import Choice
from .models import Question, Choice

# class ChoiceInline(admin, admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [( None, {'fields': ['text']} ), ('Date Information', {'fields': ['created_at'], 'classes': ['collapse']}),]
#     inlines = [ChoiceInline]

admin.site.register(Question)
admin.site.register(Choice)
