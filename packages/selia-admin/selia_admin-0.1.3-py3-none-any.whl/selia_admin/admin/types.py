from django.contrib import admin


class EventTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['should_imply']


class TermTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


class AnnotationTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ItemTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
