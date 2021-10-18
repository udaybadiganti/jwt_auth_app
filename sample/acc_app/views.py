from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from acc_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
# Create your views here.

class RegisterView(APIView):
	permission_classes = (permissions.AllowAny, )

	def post(self, request):
		try:
			data = request.data

			name = data['name']
			email = data['email']
			email = email.lower()
			password = data['password']
			re_password = data['re_password']
			is_owner = data['is_owner']

			
			print(email)

			if is_owner == 'True':
				is_owner = True
			else:
				is_owner = False

			if password == re_password:
				if len(password) >= 8:
					print("im ok")
					#print(not User.objects.filter(email=email).exists())

					if not User.objects.filter(email=email).exists():
						
						if not is_owner:
							print("it's fine5")
							User.objects.create_user(email= email, name= name, password= password)
							print("it's fine4")
							return Response({'success': 'user successfully created'}, status = status.HTTP_201_CREATED)

						else:
							print("it's fine3")
							print(User.objects.all())
							print(User.objects.create_owner(email = email, name= name, password= password))	
							print("it's fine")
							return Response({'success': 'Owner successfully created'}, status = status.HTTP_201_CREATED)
					else:
						print("uday")
						return Response({'error': 'email already exist'}, status = status.HTTP_400_BAD_REQUEST)

				else:
					return Response({'error': 'password length must be 8 char"s'},status = status.HTTP_400_BAD_REQUEST)


			else:
				return Response({'error': 'password is not matched'},status = status.HTTP_400_BAD_REQUEST)


		except:
			return Response({'error': 'something went wrong while registering........'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetriveUserView(APIView):
	def get(self, request, format=None):
		try:
			user = request.user
			user = UserSerializer(user)
			#return Response({'success': 'user successfully created'}, status = status.HTTP_201_CREATED)
			return Response({'user': user.data },status = status.HTTP_200_OK)


		except:
			return Response(
					{'error': 'something went wrong while registering.'},
					status = status.HTTP_500_INTERNAL_SERVER_ERROR
				)
