from django import forms
from .models import CreateModel

class CreateForm(forms.ModelForm):
    print("model: ")
    print(dir(CreateModel.column_type.field.choices))
    print(CreateModel.column_type.field.choices)
    # column_type = forms.ModelChoiceField(
    #     label="項目タイプ",
    #     queryset=CreateModel.objects.all(),
    #     widget=forms.RadioSelect,
    #     empty_label=None,
    # )
    # data_type = forms.ModelChoiceField(
    #     label="データタイプ",
    #     queryset=CreateModel.objects.all(),
    #     widget=forms.RadioSelect,
    #     empty_label=None,
    # )
    class Meta:
        model = CreateModel
        fields = ["column_name", "column_type", "generate_type", "link_column_name", "data_type"]
    # column_name = forms.CharFiled(max_length = 100, lebel="項目名")
    # column_type = forms.ChoiceField(
    #     choices = (
    #         ('normal', '項目作成'),
    #         ('link', 'リンク項目作成')
    #     ),
    #     label='あああ',
    #     required=True,
    #     widget=forms.widgets.RadioSelect
    # )
    # generate_type = forms.ChoiceField(
    #     choices = (
    #         ('product', '組み合わせ'),
    #         ('random', 'ランダム')
    #     ),
    #     label='いいい',
    #     required=True,
    #     widget=forms.widgets.RadioSelect
    # )
    # link_column_name = forms.CharFiled(max_length = 100, lebel="リンク項目名")
    # data_type = forms.ChoiceField(
    #     choices = (
    #         ('string', '文字'),
    #         ('number', '数値'),
    #         ('date', '日付'),
    #         ('datetime', '日時')
    #     ),
    #     label='データタイプ',
    #     required=True,
    #      widget=forms.Select(attrs={'id': 'data_type',}) 
    # )
