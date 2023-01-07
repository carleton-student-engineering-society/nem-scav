"""URLs for the management pages."""

from . import views
from django.urls import path

urlpatterns = [
    path('discord/magic-link', views.get_discord_link),
    path('users/add', views.bulk_register_users),
    path('teams', views.manage_frosh_teams, name="manage_frosh_teams"),
    path('', views.manage_index, name="manage_index"),
    path('announcements', views.announcements, name="announcements"),
    # path('roles', views.manage_roles, name="manage_roles"),
    path('scavenger/puzzles', views.manage_scavenger_puzzles, name="manage_scavenger_puzzles"),
    path('scavenger/approve-photos', views.approve_scavenger_puzzles, name="approve_scavenger_puzzles"),
    path('database/initialize', views.initialize_database, name="initialize_database"),
    path('database/scavinit', views.initialize_scav, name="initialize_scav"),
    path('trade-up/view-all', views.trade_up_viewer, name="trade_up_viewer"),
    path('users/add-to-guild', views.add_discord_user_to_guild, name="add_users_to_discord_guild"),
    path('discord/channels', views.manage_discord_channels, name="manage_discord_channels"),
    path('discord/channel-groups', views.manage_discord_channel_groups, name="manage_discord_channel_groups"),
]
