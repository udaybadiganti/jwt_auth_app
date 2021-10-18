from django.shortcuts import render
from acc_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from listing.models import Listing


class ManagingListView(APIView):
'''
	def get(self, request, format=None):
		try:
			user = request.user
			if not user.is_owner:
				return Response({'error': 'User does not have permission to retrive'},status = status.HTTP_403_FORBIDDEN)

			slug  = request.query_params.get(slug)

			if not slug:
				listing = Listing.objects.order_by('-created_date').filter(owner = user.email)

				listing = ManageListSerializer(listing, many = True)
				return Response({'listing': listing.data}, status = status.HTTP_200_OK)

		except:
			return Response({'error': 'something went wrong while registering.'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
'''
	def post(self, request):
		try:
			print("ok3")
			user = request.user
			if not user.is_owner:
				return Response({'error': 'user does not have permission to post'}, status = status.HTTP_403_FORBIDDEN)

			data = request.data
			print("ok4")
			category = data['category']
			item_name = data['item_name']
			slug = data['slug']
			#created_date = data['created_date']
			print("ok5")

			if Listing.objects.filter(slug = slug).exists():
				return Response({'error': 'Listing with this slug is already exists'}, status = status.HTTP_400_BAD_REQUEST)
			print("ok1")
			Listing.objects.create(
				category = category,
				item_name = item_name,
				slug = slug
				)
			print("ok2")
			return Response({'success': 'Items successfully created.'}, status = status.HTTP_201_CREATED)

		except:
			return Response({'error': 'Something went wrong when creating list..'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
