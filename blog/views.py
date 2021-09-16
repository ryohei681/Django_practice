from blog.models import BlogPost
from django.shortcuts import render
#from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

'''
class IndexView(TemplateView):
    トップページのビュー
    
    テンプレートのレンダリングに特化したTemplateViewを継承
    
    Attributes:
        template_name: レンダリングするテンプレート
    

    # index.htmlをレンダリングする
    template_name = 'index.html'
'''

class IndexView(ListView):
    '''トップページのビュー
    
    投稿記事を一覧表示するのでListviewを継承する
    
    Attributes:
        template_name: レンダリングするテンプレート
        context_object_name: object_listキーの別名を設定
        queryset: データベースのクエリ
    '''

    # index.htmlをレンダリングする
    template_name = 'index.html'
    #context_object_name: object_listキーの別名を設定
    context_object_name = 'orderby_records'
    #モデルBlogPostのオブジェクトにorder_by()を適用してBlogPostのレコードを投稿日時の降順で並び替える
    queryset = BlogPost.objects.order_by('-posted_at')

class BlogDetail(DetailView):
    '''詳細ページのビュー
    投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
        template_name: レンダリングするテンプレート
        Model: モデルのクラス
    '''
    # post.htmlをレンタリングする
    template_name ='post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost