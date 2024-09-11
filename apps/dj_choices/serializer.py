from rest_framework import serializers
from .models import SY, Department
from django.db.models import Max



class SYSerializer(serializers.ModelSerializer):
    # roll_no = serializers.IntegerField(required=False)
    apaka_department = serializers.CharField(source='department')
    class Meta:
        model = SY
        fields = '__all__'

    # This method get called when we want to serialize model instance. when we use .data method on serialzier insatnce. data = SYSerializer(model).data
    def to_representation(self, instance):
        print('to_representation, fetching the model from DB.')
        data = super().to_representation(instance)

        data['department_name'] = instance.department.name
        data['result'] = 'Pass' if instance.marks and instance.marks > 35 else 'Fail'
        return data

    # call: .is_valid() while deserialize the data. seri = SYSerializer(data=data) then user .save() method.
    def to_internal_value(self, data):
        print('to_internal_value, saving the instance data into DB')
        data['marks'] = data['marks']+5 if data['marks'] else 35
        return super().to_internal_value(data)
    
    def create(self, validated_data):
        print('creating the instance...')

        if not self.roll_no:
            current_max = SY.objects.filter(division=self.division).aggregate(Max('roll_no', default=0))
            self.roll_no = current_max['roll_no__max'] + 1
        
        validated_data['marks'] += 5
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        print('updating the insance...')
        return super().update(instance, validated_data)
    
    # call: .is_valid(). While deserialzing the data we must have to call .is_valid() method before saving.
    def validate(self, attrs):
        print('validating the data....')
        if attrs['marks'] is None:
            raise serializers.ValidationError('Marks should not be null.')
        return super().validate(attrs)
    
    # call: .save(). If we don't pass model object in input then this save calls .create() method, otherwise this save calls .update() method.
    def save(self, **kwargs):
        print('saving the instance....')
        return super().save(**kwargs)



class DepSerializer(serializers.ModelSerializer):
    students = SYSerializer(source='sy_set', many=True)
    class Meta:
        model = Department
        fields = '__all__'