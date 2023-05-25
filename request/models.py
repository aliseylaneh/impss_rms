from django.db import models
from django_fsm import FSMField
from common.db.basic import Logged
from django.utils.translation import gettext_lazy as _


class RequestStateChoices(models.TextChoices):
    STARTING = "CT", _("Created")
    PROCESSING = "PR", _("Processing")
    COMPLETED = "CO", _("Completed")


class Request(Logged):
    provincial_organization = models.PositiveIntegerField(_("Provincial Organization"), null=False)
    provincial_prison = models.PositiveIntegerField(_("Provincial Prison"), null=False)
    state = FSMField(choices=RequestStateChoices.choices, default=RequestStateChoices.STARTING)
