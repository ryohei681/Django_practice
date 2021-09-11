from django.urls import path
from . import views

# URLパターンを逆引きできるように名前をつける
app_name = 'blog'

# URLパターンを登録するための変数
# リクエストされたURLのページへのフルパス部分が''(無し)にマッチングした場合
# viewsモジュールのIndexcViewクラスをインスタンス化する
urlpatterns = {
    path('', views.IndexView.as_view(), name='index'),
}