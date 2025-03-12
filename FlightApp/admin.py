from django.contrib import admin
from .models import Pilot, Airline, AirLinePilot, Balloon, Flight


# Register your models here.
class AirLinePilotInline(admin.TabularInline):
    model = AirLinePilot
    extra = 0

class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name", "year_founded", "outside_of_Europe")
    inlines = [AirLinePilotInline]

    def has_add_permission(self, request):
        return True

class PilotAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname")

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Flight, FlightAdmin)
admin.site.register(Balloon)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Airline, AirlineAdmin)