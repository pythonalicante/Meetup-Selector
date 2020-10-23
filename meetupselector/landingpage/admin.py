from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import LandingPageContent

# Apply summernote to all TextField in model.
class LandingPageContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(LandingPageContent, LandingPageContentAdmin)