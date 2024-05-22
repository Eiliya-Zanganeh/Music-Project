from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name='user_view'),
    path('register/', RegisterView.as_view(), name='register_view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('musics/', GetAllMusicView.as_view(), name='musics'),
    path('delete-music/<int:music_id>/', DeleteMusicView.as_view(), name='detail_music'),
    path('update-music/', UpdateMusicView.as_view(), name='update_music'),
    path('all-musics/', AllMusicView.as_view(), name='all_music'),
    path('music-detail/<int:id>/', MusicDetailView.as_view(), name='music_detail'),
    path('add-comment/', AddCommentView.as_view(), name='add_comment'),
]
