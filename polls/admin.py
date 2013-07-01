from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('poll', 'choice_text', 'votes')

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
# admin.site.register(Choice)