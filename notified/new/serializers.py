from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'name', 'notification_type', 'notified_person', 'notification_status', 'created_at', 'updated_at', 'deleted_at', 'is_active', 'is_deleted']


