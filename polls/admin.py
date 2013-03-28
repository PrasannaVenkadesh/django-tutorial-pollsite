from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	'''fieldsets = [
		(None, {'fields':['question']}),
		('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]'''

	list_display = ('question','pub_date','was_recently_published')
	list_filter = ['pub_date']
	search_fields = ['question']
	inlines = [ChoiceInline]
	date_hierarchy = 'pub_date'

	#fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)