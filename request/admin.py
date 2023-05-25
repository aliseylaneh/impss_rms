from django.contrib import admin
from common.admin_registery.admin import DefaultAdminMixin

from request.models import Request
from fsm_admin.mixins import FSMTransitionMixin


# Register your models here.

@admin.register(Request)
class OrderPaymentTransactionAdmin(FSMTransitionMixin, DefaultAdminMixin, admin.ModelAdmin):
    fsm_field = ['state', ]
    list_display = ["order_id", "national_code", "entity_id", "amount", "state", "phone_number"]
    search_fields = ["entity_id", "order_id", "national_code", "phone_number"]
    list_filter = ["type", "state"]
