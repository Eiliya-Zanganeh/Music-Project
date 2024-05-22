from django.db.models import Count
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from User_Module.serializer import UserSerializer, MusicSerializer, CommentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from User_Module.models import UserModel as User, MusicModel, CommentModel


class RegisterView(APIView):
    def post(self, request: Request):
        user: User = User.objects.filter(email=request.data['email']).first()
        if user is None:
            new_user: User = User(
                first_name=request.data['name'],
                username=request.data['email'],
                email=request.data['email'],
                age=request.data['age'],
                country=request.data['country'],
                is_active=False
            )
            new_user.set_password(request.data['password'])
            new_user.save()
            # Todo Send Email active code
            return Response({"Message": "User Created"}, status.HTTP_201_CREATED)

        else:
            return Response({"Error": "User Already Exists"}, status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user = request.user
        data = UserSerializer(user)
        return Response({"first_name": data.data['first_name']}, status=status.HTTP_200_OK)


class UploadFileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        i = 0
        while True:
            try:
                file = request.FILES[str(i)]
                filename = file.name.strip('/medias/musics/')
                filename = filename.split('.')[0]
                serializer = MusicSerializer(data={'user': request.user.id, 'music': file, 'title': filename})
                if serializer.is_valid():
                    serializer.save()
            except MultiValueDictKeyError:
                break
            i += 1
        return Response({"msg": "ok"}, status=status.HTTP_201_CREATED)


class GetAllMusicView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        musics = MusicModel.objects.filter(user=request.user)
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteMusicView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return MusicModel.objects.get(pk=id)
        except MusicModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, music_id: int):
        music = self.get_object(music_id)
        music.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class UpdateMusicView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        try:
            music = MusicModel.objects.get(pk=request.data['id'])
            music.title = request.data['title']
            music.save()
            return Response(None, status.HTTP_200_OK)
        except MusicModel.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)


class AllMusicPagination(PageNumberPagination):
    page_size = 1


class AllMusicView(generics.ListAPIView):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializer
    pagination_class = AllMusicPagination


class MusicDetailView(APIView):
    def get(self, request: Request, id):
        music = MusicModel.objects.filter(pk=id).first()
        music_serializer = MusicSerializer(music)
        comments = CommentModel.objects.filter(music=id).order_by('date')
        comment_serializer = CommentSerializer(comments, many=True)
        return Response({"music": music_serializer.data, "comments": comment_serializer.data}, status=status.HTTP_200_OK)


class AddCommentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request:Request):
        user = request.user
        music = MusicModel.objects.filter(id=request.data['music']).first()
        text = request.data['comment']
        comment = CommentModel(user=user, music=music, text=text)
        comment.save()
        return Response(None, status.HTTP_201_CREATED)
