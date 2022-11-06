from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin
from .models import News, NewsImages, Contact, Calendar, Coach, Hall, Video
from django.contrib import messages
from django.utils.translation import ngettext


class NewsImagesInline(admin.TabularInline):
    fk_name: "News"
    model = NewsImages
    readonly_fields = ["get_photo"]

    def get_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    get_photo.short_description = 'Фото'


class NewsAdmin(SummernoteModelAdmin):
    actions = ['move_to_archive', 'move_from_archive']

    summernote_fields = ('text',)
    list_display = ('pk', 'title', 'preambule',
                    'get_prev_photo', 'created_at', 'deleted')
    fields = ('title', 'preambule', 'text',
              ('main_picture', 'get_prev_photo'), 'deleted')
    readonly_fields = ['get_prev_photo']
    list_filter = ('deleted', 'created_at')
    ordering = ('-created_at',)
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

    @admin.action(description='Перенести в архив')
    def move_to_archive(self, request, queryset):
        queryset.update(deleted=True)

        updated = queryset.update(deleted=True)
        self.message_user(request, ngettext(
            '%d новость была успешно перенесена в архив!',
            '%d новостей были успешно перенесены в архив!',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Опубликовать')
    def move_from_archive(self, request, queryset):
        queryset.update(deleted=False)

        updated = queryset.update(deleted=False)
        self.message_user(request, ngettext(
            '%d новость была успешно опубликована!',
            '%d новостей были успешно опубликованы!',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('parents_name', 'age',
                    'phone_number', 'request_date', 'is_contacted')
    list_filter = ('request_date', 'is_contacted')
    ordering = ('-request_date', )
    list_per_page = 15
    search_fields = ('parents_name', 'child_name')
    date_hierarchy = ('request_date')


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):

    actions = ['move_to_archive', 'move_from_archive']

    list_display = ('title', 'date',
                    'city', 'in_archive')
    list_filter = ('in_archive', 'city')
    ordering = ('-date', )
    list_per_page = 10
    search_fields = ('city',)
    date_hierarchy = ('date')

    @admin.action(description='Перенести в архив')
    def move_to_archive(self, request, queryset):
        queryset.update(in_archive=True)

        updated = queryset.update(in_archive=True)
        self.message_user(request, ngettext(
            '%d соревнование было успешно перенесено в архив!',
            '%d соревнования были успешно перенесены в архив!',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Сделать соревнование предстоящим')
    def move_from_archive(self, request, queryset):
        queryset.update(in_archive=False)

        updated = queryset.update(in_archive=False)
        self.message_user(request, ngettext(
            '%d соревнование изменило статус на предстоящее!',
            '%d соревнования изменили статус на предстоящее!',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('pk', 'placement',)
    list_per_page = 10
    search_fields = ('placement',)


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('pk', 'last_name', 'first_name', 'father_name', )
    list_per_page = 10
    search_fields = ('placement',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date',)
    list_per_page = 10
    search_fields = ('title',)


admin.site.site_title = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.site_header = 'Костромская Федерация Тхэквондо-ИТФ'
admin.site.register(News, NewsAdmin)
