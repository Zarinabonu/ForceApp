from rest_framework.serializers import ModelSerializer

from app.model.school import School


class SchoolListSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ('id',
                  'name',
                  )