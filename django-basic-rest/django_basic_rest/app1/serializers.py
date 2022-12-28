from rest_framework import serializers
from .models import Todo, Note

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "timestamp","completed", "updated", "user"]


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["text", "type", "todo"]