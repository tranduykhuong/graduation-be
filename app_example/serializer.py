from rest_framework import serializers
from .models import Wisher

RELATIONSHIP_MAPPING = {
    "bạn": "mình",
    "cậu": "con",
    "mợ": "con",
    "dì": "con",
    "dượng": "con",
    "chú": "con",
    "bác": "con",
    "anh": "em",
    "em": "anh",
    "chị": "em",
    "cháu": "con",
    "thầy": "em/con",
    "cô": "em/con",
    "bà": "con",
    "ông": "con"
}

class WisherSerializer(serializers.ModelSerializer):
    mapped_relationship = serializers.SerializerMethodField()

    class Meta:
        model = Wisher
        fields = [
            'id', 'key', 'last3phone', 'name', 'email', 'relationship',
            'mapped_relationship', 'img_url', 'wisher', 'confirm', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_mapped_relationship(self, obj):
        return RELATIONSHIP_MAPPING.get(obj.relationship, "Khương")
