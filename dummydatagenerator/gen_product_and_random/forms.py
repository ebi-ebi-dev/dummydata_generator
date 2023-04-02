from django import forms
from .models import Post

DEFAULT_JSON ="""[
{"column_name": "文字", "generate_type": "product", "generate_data": ["aaa", "bbb", "ccc"]},
{"column_name": "数値", "generate_type": "random", "generate_data": [100, 250, 300]},
{"column_name": "日付", "generate_type": "product", "generate_data": ["2023/03/13", "2023/03/14", "2023/03/15"]},
{"column_name": "日時", "linked_cname": "日付", "generate_data": ["2023/03/13 10:00:00", "2023/03/14 10:00:00", "2023/03/15 10:00:00"]}
]
"""

class DocumentForm(forms.Form):

    document = forms.FileField()

class JSONForm(forms.Form):
    text = forms.CharField(
        # initial = DEFAULT_JSON, <- 機能しない
        label = "JSONテキストを入力",
        required=True,
        widget = forms.Textarea(attrs={
            'placeholder': DEFAULT_JSON, 
            "class" : "form-control",
        }),
    )