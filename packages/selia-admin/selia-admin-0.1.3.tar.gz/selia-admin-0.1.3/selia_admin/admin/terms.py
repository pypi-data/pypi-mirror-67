from django.contrib import admin


class TermAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['term_type']


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
