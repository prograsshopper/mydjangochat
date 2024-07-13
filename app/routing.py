from django.urls import path
from app.consumers import EchoConsumer, LiveblogConsumer


'''
장고의 urls - urlpatterns와 유사한 역할
장고 기본에 있는 것과 다르게 이는 장고는 알아서 찾아가는게 아니라
우리가 asgi 에 정의한대로 직접 임포트하여 지정하기에 다른 이름이어도 됨
'''
websocket_urlpatterns = [
    path("ws/liveblog/", LiveblogConsumer.as_asgi()),
    path("ws/echo/", EchoConsumer.as_asgi()),
]