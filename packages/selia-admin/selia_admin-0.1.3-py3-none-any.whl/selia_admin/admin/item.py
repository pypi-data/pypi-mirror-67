from django.contrib import admin


def get_site(item):
    sampling_event = item.sampling_event_device.sampling_event
    return sampling_event.collection_site.internal_id


class ItemAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = ['id']
    list_display = (
        'id',
        'item_type',
        'collection',
        get_site,
        'captured_on',
        'created_on')
    autocomplete_fields = [
        'item_type',
        'sampling_event_device',
        'tags',
        'ready_event_types']

    fieldsets = (
        (None, {
            'fields': (
                ('item_type', 'sampling_event_device', 'licence'),
                ('tags', 'ready_event_types'),
            )
        }),
        ('Date and time of capture', {
            'classes': ('collapse', ),
            'fields': (
                'captured_on',
                'captured_on_timezone',
                ('captured_on_year', 'captured_on_month', 'captured_on_day'),
                ('captured_on_hour', 'captured_on_minute', 'captured_on_second'),
            )
        }),
        ('Media info', {
            'classes': ('collapse', ),
            'fields': (
                ('filesize', 'hash'),
                'media_info'
            )
        }),
        ('Files', {
            'classes': ('collapse', ),
            'fields': ('item_file', 'item_thumbnail')
        }),
        ('Metadata', {
            'classes': ('collapse', ),
            'fields': ('metadata',)
        }),
    )
