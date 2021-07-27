from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class ListModel(models.Model):
    user_id = models.ForeignKey(User, related_name="user_list", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=800)
    quantity = models.CharField(max_length=300)
    class Status(models.TextChoices):
        BOUGHT = 'BOUGHT', _('item_bought')
        NOT_AVAILABLE = 'NOT AVAILABLE', _('item_end')
        PENDING = 'PENDING', _('in_queue')
    action = models.CharField(max_length=20, choices=Status.choices)
    created_at = models.DateTimeField(blank=True, null=True)