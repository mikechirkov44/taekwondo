from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import News, NewsImages, Contact, Calendar


class NewsImagesInline(admin.TabularInline):
    fk_name: "News"
    model = NewsImages
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_photo.short_description = 'Фото'


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('pk', 'title', 'preambule', 'get_prev_photo', 'deleted')
    fields = ('title', 'preambule', 'text',
              ('main_picture', 'get_prev_photo'), 'deleted')
    readonly_fields = ['get_prev_photo']
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    list_per_page = 5
    search_fields = ('title', 'preambule', 'text')
    date_hierarchy = ('created_at')
    inlines = [NewsImagesInline]

    def get_prev_photo(self, object):
        if object.main_picture:
            return mark_safe(f"<img src='{object.main_picture.url}' width=80 height=100>")
    get_prev_photo.short_description = ''

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('parents_name', 'age',
                    'phone_number', 'request_date', 'is_contacted')
    list_filter = ('request_date', 'is_contacted')
    ordering = ('-request_date', )
    list_per_page = 10
    search_fields = ('parents_name', 'child_name')
    date_hierarchy = ('request_date')


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',
                    'city', 'in_archive')
    list_filter = ('in_archive', 'city')
    ordering = ('-date', )
    list_per_page = 10
    search_fields = ('city',)
    date_hierarchy = ('date')


admin.site.site_title = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.site_header = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.register(News, NewsAdmin)
