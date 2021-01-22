from django.contrib import admin
from .models import Notification
# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'notification_type', 'notified_person', 'notification_status', 'created_at', 'updated_at', 'deleted_at', 'is_active', 'is_deleted']
