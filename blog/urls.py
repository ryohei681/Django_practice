from django.urls import path
from . import views

# URLパターンを逆引きできるように名前をつける
app_name = 'blog'

# URLパターンを登録するための変数
# リクエストされたURLのページへのフルパス部分が''(無し)にマッチングした場合
# viewsモジュールのIndexcViewクラスをインスタンス化する
urlpatterns = [
    #リクエストされたURLが''(無し)の場合
    #viewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    #リクエストされたURが「blog-detail/レコードのid/」の場合はBlogDetailを実行
    path(
        #詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        #viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        #URLパターンの名前を'blog_detail'にする
        name='blog_detail'
    ),
]