from django.contrib import admin

# Register your models here.
from .models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

admin.site.register(Conversation, ConversationAdmin)