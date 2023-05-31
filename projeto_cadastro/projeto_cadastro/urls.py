
from django.urls import path
from app_cadastro import views

urlpatterns = [

    #instagram.com
    # github.com/jucmo123
    # rota, view, nome de referência
    path('',views.home, name='home') # cria a rota -> ir no arquivo 'views.py' e criar a página



]
