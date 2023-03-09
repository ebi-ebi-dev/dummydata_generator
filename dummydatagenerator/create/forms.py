from django import forms
from .models import CreateModel

class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateModel
        fields = ("__all__")
        # fields = ["column_name", "column_type", "generate_type", "link_column_name", "data_type"]
    
    column_name = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder':'項目名', }),
        initial='Text'
    )
    column_type = forms.ChoiceField(
        choices = (
            ('normal', '項目作成'),
            ('link', 'リンク項目作成')
        ),
        label='あああ',
        required=True,
        widget=forms.widgets.RadioSelect(attrs = {"class": "test_class"}),
        initial='normal'
    )
    generate_type = forms.ChoiceField(
        choices = (
            ('product', '組み合わせ'),
            ('random', 'ランダム')
        ),
        label='いいい',
        required=True,
        widget=forms.widgets.RadioSelect,
        initial = "product"
    )
    link_column_name = forms.CharField(max_length = 100)
    data_type = forms.ChoiceField(
        choices = (
            ('string', '文字'),
            ('number', '数値'),
            ('date', '日付'),
            ('datetime', '日時')
        ),
        label='データタイプ',
        required=True,
        widget=forms.Select(attrs={'id': 'data_type',}) ,
        initial='date'
    )

    import datetime
    text = forms.CharField(
        initial = "aaaa",
        widget=forms.Textarea()
    )

    number_min = forms.FloatField()
    number_max = forms.FloatField()
    number_step = forms.FloatField()

    date_min = forms.DateField(
        label='最小日付',
        required=False,        
        initial = datetime.date.today()
    )
    date_max = forms.DateField(
        label='最大日付',
        required=False,        
        initial = datetime.date.today() + datetime.timedelta(days=10)
    )
    date_step = forms.IntegerField(
        label='ステップ（日）',
        required=False,        
        initial = 1
    )

    datetime_min = forms.DateTimeField(
        label='最小日時',
        required=False,        
        initial = datetime.datetime.now()
    )
    datetime_max = forms.DateTimeField(
        label='最大日時',
        required=False,        
        initial = datetime.datetime.now() + datetime.timedelta(days=1)
    )
    datetime_step = forms.IntegerField(
        label='ステップ（秒）',
        required=False,        
        initial = 60
    )

    # text = forms.Textarea()

    # number_min = forms.FloatField()
    # number_max = forms.FloatField()
    # number_step = forms.FloatField()

    # date_min = forms.IntegerField()
    # date_max = forms.IntegerField()

    # datetime_min = forms.IntegerField()
    # datetime_max = forms.IntegerField()