from django.contrib import admin

from api.models.event import Events
from .models.custom_user import User
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "nickname",
        "is_active",
        "is_staff",
    )

@admin.register(Events)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "event_title",
        "location",
        "start_time",
        "end_time",
    )
