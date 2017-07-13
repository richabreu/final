from django.contrib import admin
from final.models import User, SourceTag, SourceUrl

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

#admin.site.register(Category)
#admin.site.register(Page)
#admin.site.register(Page, PageAdmin)
admin.site.register(User)
#admin.site.register(UserProfile)
admin.site.register(SourceTag)
admin.site.register(SourceUrl)
# Register your models here.
