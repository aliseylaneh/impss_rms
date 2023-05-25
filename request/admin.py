from django.contrib import admin

from request.models import Request
from fsm_admin.mixins import FSMTransitionMixin


# Register your models here.

@admin.register(Request)
class RequestAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = ['state', ]
    list_display = ["id", "provincial_organization", "provincial_prison", "state"]
    search_fields = ["id", "provincial_organization", "provincial_prison"]
    list_filter = ["id", "state"]
