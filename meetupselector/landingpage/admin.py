from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Collaborator, Content, SocialNetwork


# Apply summernote to all TextField in model.
class ContentAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "__all__"


class SocialNetworkInLine(admin.TabularInline):

    model = SocialNetwork
    extra = 0


class CollaboratorAdmin(admin.ModelAdmin):

    model = Collaborator
    inlines = [SocialNetworkInLine]
    list_display = (
        "first_name",
        "last_name",
        "email",
        "nationality",
        "_social_network",
    )

    def queryset(self, request):
        return (
            super(CollaboratorAdmin, self)
            .queryset(request)
            .select_related("social_network")
        )

    def _social_network(self, obj):
        return obj.social_network.all().count()


admin.site.register(Content, ContentAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
