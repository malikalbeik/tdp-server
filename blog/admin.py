from django.contrib import admin
from .models import Post, Image

# Register your models here.


class ImagesInLine(admin.TabularInline):
    model = Image
    extra = 0


def has_approval_permission(request):
    print("the user has the right: {}".format(request.user.has_perm('blog.can_publish')))
    if request.user.has_perm('blog.can_publish'):
        return True
    return False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 
    list_display = ("title", "summary", "date_created", "is_published")
 
    inlines = [
        ImagesInLine
    ]




    def get_form(self, request, obj=None, **kwargs):
        if has_approval_permission(request):
            kwargs['fields'] = ['title', 'coverImage',
                                'project', 'summary', 'content',
                                'is_published', 'date_published']
        else:
             kwargs['fields'] = ['title', 'coverImage',
                                 'project', 'summary', 'content']
        return super(PostAdmin, self).get_form(request, obj, **kwargs)

