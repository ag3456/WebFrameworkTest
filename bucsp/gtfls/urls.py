from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.parameterform, name='parameterform'),
    path('dispfiles/', views.dispfiles, name='dispfiles'), #dispfiles is its view
    path('dispfiles/<int:experimentid>/', views.fndwnld, name='fndwnld'), #recieve the experiment id and display the files, fndwnld is its view
	path('dispfiles/<int:experimentid>/<expName>/', views.downloadfiles, name = 'downloadfiles'),
]
