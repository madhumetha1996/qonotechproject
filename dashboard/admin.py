from django.contrib import admin
from .models import Dashboard

# Define your custom admin configurations here
class DashboardAdmin(admin.ModelAdmin):
    # Customizations for the Dashboard model in the admin site
    # Add any customizations you want, such as list_display, list_filter, search_fields, etc.
    list_display = ['title', 'description']

# Register the Dashboard model with the custom admin configurations
admin.site.register(Dashboard, DashboardAdmin)
