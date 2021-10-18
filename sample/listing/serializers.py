from rest_framework import serializers
from listing.models import Listing

class ManageListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = '__all__'