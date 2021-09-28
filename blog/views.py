from blog.models import BlogPost
from django.shortcuts import render
#from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages

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
    # 1ページに表示するレコードの件数
    paginate_by = 2

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

class ScienceView(ListView):
    '''科学(science)カテゴリの記事を一覧表示するビュー
    
    '''
    # science_list.htmlをレンダリングする
    template_name = 'science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # cotegory='scienceのレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    # 1ページの表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常(dailylife)カテゴリの記事を一覧表示するビュー
    
    '''
    # dailylife_list.htmlをレンダリングする
    template_name = 'dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # cotegory='dailylife'のレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    # 1ページの表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽(music)カテゴリの記事を一覧表示するビュー
    
    '''
    # music_list.htmlをレンダリングする
    template_name = 'music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # cotegory='music'のレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    # 1ページの表示するレコードの件数
    paginate_by = 2

class ContactView(FormView):
    '''問い合わせページを一覧表示するビュー
    
    '''
    # contact.htmlをレンダリングする
    template_name = 'contact.html'
    # クラス変数form_classにforms.pyで定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド
        フォームの検証を通過したデータがPOSTされたときに呼ばれる
        メール送信を行う
        
        parameters:
            form(django.forms.Form):
                form_classに格納されているフォームのオブジェクト
        Return:
            HttpResponseRedirectのオブジェクト
            オブジェクトをインスタンス化するとsuccess_urlで
            設定されているURLにリダイレクトされる
        '''
        # forms.pyのsend_email()を実行してメール送信を行う
        form.send_email()
        # 送信完了後に表示するメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。'
        )
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


    
    