from django.contrib import admin
from .models import Group, Membership,GroupChatMessage,Profile

# Register your models here.
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(GroupChatMessage)
admin.site.register(Profile)
