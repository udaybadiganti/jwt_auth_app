from django.shortcuts import render
from acc_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from listing.models import Listing
from listing.serializers import ManageListSerializer


class ManagingListView(APIView):

	def get(self, request, format=None):
		try:
			user = request.user
			if not user.is_owner:
				return Response({'error': 'User does not have permission to retrive'},status = status.HTTP_403_FORBIDDEN)

			#retriving form api arguments params
			slug  = request.query_params.get('slug')

			if not slug:
				listing = Listing.objects.order_by('-created_date').filter(owner = user.email)
				listing = ManageListSerializer(listing, many = True)
				return Response({'listing': listing.data}, status = status.HTTP_200_OK)

			if not Listing.objects.filter(owner = user.email, slug = slug).exists():
				return Response({'error': 'Listing not available.'}, status = status.HTTP_404_NOT_FOUND)
			
			listing = Listing.objects.filter(owner = user.email, slug = slug)
			listing = ManageListSerializer(listing, many = True)
			print("udays")
			print(listing.data)

			return Response({'listing': listing.data}, status = status.HTTP_200_OK)


		except:
			return Response({'error': 'something went wrong while registering.'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
		
	def post(self, request):
		try:
			user = request.user
			if not user.is_owner:
				return Response({'error': 'user does not have permission to post'}, status = status.HTTP_403_FORBIDDEN)

			data = request.data
			print(data.keys())
			category = data['category']
			item_name = data['item_name']
			slug = data['slug']
			#created_date = data['created_date']

			if Listing.objects.filter(slug = slug).exists():
				return Response({'error': 'Listing with this slug is already exists'}, status = status.HTTP_400_BAD_REQUEST)
			
			Listing.objects.create(
				owner = user.email,
				category = category,
				item_name = item_name,
				slug = slug
				)
			
			return Response({'success': 'Items successfully created.'}, status = status.HTTP_201_CREATED)

		except:
			return Response({'error': 'Something went wrong when creating list..'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

	def retrive_values(self, data):

		category = data['category']
		item_name = data['item_name']
		slug = data['slug']

		data = {
			'category': category,
			'item_name': item_name,
			'slug': slug
		}
		return data

	def put(self, request):
		try:
			user = request.user

			if not user.is_owner:
				return Response({'error': 'User does not have permission to create items.'}, status = status.HTTP_400_BAD_REQUEST)

			data = request.data


			data = self.retrive_values(data)

			category = data['category']
			item_name = data['item_name']
			slug = data['slug']

			if not Listing.objects.filter(slug = slug).exists():
				return Response({'error': 'Listing with this slug is already exists'}, status = status.HTTP_400_BAD_REQUEST)

			Listing.objects.create(
				owner = user.email,
				category = category,
				item_name = item_name,
				slug = slug
				)
			return Response({'success': 'Items successfully created.'}, status = status.HTTP_201_CREATED)


		except:
			return Response({'error': 'Something went wrong when creating list..'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

	def delete(self, request):
		try:
			user = request.user

			if not user.is_owner:
				return Response({'error': 'User does not have permission to create items.'}, status = status.HTTP_400_BAD_REQUEST)

			slug = request.query_params.get('slug')
			#print(slug)

			if not Listing.objects.filter(owner = user.email, slug = slug).exists():
				return Response({'error': 'Listing slug is not available'}, status = status.HTTP_400_BAD_REQUEST)

			Listing.objects.filter(owner=user.email, slug=slug).delete()

			if not Listing.objects.filter(owner=user.email, slug=slug).exists():
				return Response(status=status.HTTP_204_NO_CONTENT)
			else:
				return Response({'error': 'Failed to delete listing'},status=status.HTTP_400_BAD_REQUEST)
			


		except:
			return Response({'error': 'Something went wrong when creating list..'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


'''
	def retrive_values_patch(self, data):
		pass

	def patch(self, request):
		try:
			user = request.user

			if not user.is_owner:
				return Response({'error': 'User does not have permission to create items.'}, status = status.HTTP_400_BAD_REQUEST)

			data = request.data

			data = self.retrive_values_patch(data)

			if slug	

		except:
			return Response({'error': 'Something went wrong when creating list..'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
'''