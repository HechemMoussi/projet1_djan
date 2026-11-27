from django.contrib import admin
from AppointmentApp.models import Appointment
# Register your models here.
@admin.register(Appointment)
class AppointmentAdminPersonaliser(admin.ModelAdmin):
    list_display = (
        "id","status","reason","prescription",
        "duration_minutes","created_at","updated_at","doctor","patient",
)
    list_filter = ("status", "doctor", "patient")
    search_fields = ("reason", "doctor__user__username", "patient__user__username")