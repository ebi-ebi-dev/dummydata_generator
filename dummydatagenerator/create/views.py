from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CreateForm
from django import forms

FORM_NUM = 1      # フォーム数
FORM_VALUES = {}  # 前回のPSOT値

class MyCreate(FormView):
    template_name = 'create.html'
    success_url = reverse_lazy('create')
    form_all = forms.formset_factory(
        form = CreateForm,
        extra=1,
        max_num=10,
    )
    form_class = form_all
    print(FORM_NUM)

    def get_form_kwargs(self):
        print(FORM_NUM)
        # デフォルトのget_form_kwargsメソッドを呼び出す
        kwargs = super().get_form_kwargs()
        # FORM_VALUESが空でない場合（入力中のフォームがある場合）、dataキーにFORM_VALUESを設定
        if FORM_VALUES:
            kwargs['data'] = FORM_VALUES
        return kwargs

    def post(self, request, *args, **kwargs):
        global FORM_NUM
        global FORM_VALUES
        # 追加ボタンが押された時の挙動
        if 'add_box' in request.POST:
            print("pushed add_box button", request.POST)
            FORM_NUM += 1    # フォーム数をインクリメント
            FORM_VALUES = request.POST.copy()  # リクエストの内容をコピー
            FORM_VALUES['form-TOTAL_FORMS'] = FORM_NUM   # フォーム数を上書き
        
        return super().post(request, args, kwargs)

# def create(request):
#     posts = CreateModel.objects.all()
#     forms_all = CreateForm()
#     forms_normal = CreateDataConfigForm()
#     forms_link = CreateLinkDataConfigForm()
    
#     # print("posts: ")
#     # print(posts)
#     # print("forms: ")
#     print(forms)
#     TestFormSet = forms.formset_factory(
#             form = CreateForm,
#             extra = 3,     # default-> 1
#             max_num = 10    # initial含めformは最大4となる
#     )

    
#     if request.method == 'POST':
#         if(forms_all.is_valid()):
#             data = repr(forms_all.cleaned_data)
#             return HttpResponse(data) 
#             return redirect('http://localhost:8000/create/check/')

#     else:
#         formset = TestFormSet() # initialを渡すことができます。
#         content = {
#             "posts" : posts,
#             "forms" : forms_all,
#             "forms_normal" : forms_normal,
#             "forms_link" : forms_link,
#         }
#     return render(request, 'create.html', content)

def check(request):
    return render(request, 'check.html', {})