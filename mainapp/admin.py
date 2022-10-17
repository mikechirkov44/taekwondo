from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import News, NewsImages, Contact


class NewsImagesInline(admin.TabularInline):
    fk_name: "News"
    model = NewsImages


class NewsAdmin(SummernoteModelAdmin):

    summernote_fields = ('text', )

    list_display = ('pk', 'title', 'preambule', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk', )
    list_per_page = 3
    search_fields = ('title', 'preambule', 'text')
    date_hierarchy = ('created_at')
    inlines = [NewsImagesInline]

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)
    mark_as_delete.short_description = 'Пометить удаленным'


admin.site.site_title = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.site_header = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.register(News, NewsAdmin)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('parents_name', 'age',
                    'phone_number', 'request_date', 'is_contacted')
    list_filter = ('request_date', 'is_contacted')
    ordering = ('-request_date', )
    list_per_page = 3
    search_fields = ('parents_name', 'child_name')
    date_hierarchy = ('request_date')
