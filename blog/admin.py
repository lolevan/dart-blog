from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'slug', 'category', 'author', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('content', 'author', 'title')
    list_filter = ('category', 'author', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'category', 'tags', 'author', 'content', 'created_at', 'photo', 'get_photo', 'views')
    readonly_fields = ('created_at', 'views', 'get_photo')
    save_as = True
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
