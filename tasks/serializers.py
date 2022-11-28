from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task']


    def create(self, validated_data):
        instance = Task()
        instance.task = validated_data['task']
        instance.create()
        return instance

    def update(self, instance, validated_data):
        instance.task = validated_data['task']
        instance.new_order_no = int(validated_data['order_no'])
        instance.save()
        return instance