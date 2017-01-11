from django.contrib import admin
from .models import Game, UserProfile

class GameAdmin(admin.ModelAdmin):
    fields = [
        'game_name', 'game_description'
    ]

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Profile Picture', {'fields': ['Profile Picture']}),
        ('Profile', {'fields': ['detail', 'dob', 'level']})
    ]


admin.site.register(Game, GameAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
