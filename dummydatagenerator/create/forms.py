from django import forms
from .models import CreateModel

class ColumnNameForm(forms.Form):
    
    column_name = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder':'項目名', 
            "onchange" : "set_columnname(this.id)"
        }),
        label = "項目名",
    )

class ColumnTypeForm(forms.Form):
    
    column_type = forms.ChoiceField(
        choices = (
            ('', '項目タイプを選択'),
            ('normal', '項目作成'),
            ('link', 'リンク項目作成')
        ),
        label='項目タイプ',
        required=True,
        widget=forms.widgets.Select(attrs = {
            "id" : "column_type",
            "onchange" : "set_columntype(this.id)"
        }),
        # initial='normal'
    )


class NormalForm(forms.Form):
    generate_type = forms.ChoiceField(
        choices = (
            ('', '生成タイプを選択'),
            ('product', '組み合わせ'),
            ('random', 'ランダム')
        ),
        label='生成タイプ',
        required=True,
        widget=forms.widgets.Select(attrs={
            "onchange" : "set_generatetype(this.id)"
        }),
        # initial = "product"
    )
    data_type = forms.ChoiceField(
        choices = (
            ("", "データタイプを選択"),
            ('string', '文字'),
            ('number', '数値'),
            ('date', '日付'),
            ('datetime', '日時')
        ),
        label='データタイプ',
        required=True,
        widget=forms.Select(attrs={
            "onchange" : "set_datatype(this.id)",
        }) ,
    )

class LinkForm(forms.Form):

    link_column_name = forms.CharField(
        max_length = 100, 
        label = "リンク項目名",
        widget = forms.TextInput(attrs={
            'placeholder':'リンク項目名', 
            "onchange" : "set_link_columnname(this.id)"
        }),

    )
    data_type = forms.ChoiceField(
        choices = (
            ("", "データタイプを選択"),
            ('string', '文字'),
            ('number', '数値'),
            ('date', '日付'),
            ('datetime', '日時')
        ),
        label='データタイプ',
        required=True,
        widget=forms.Select(attrs={
            "onchange" : "set_datatype(this.id)",
        }),
    )

class NormalDataTypeForm_Text(forms.Form):
    
    text = forms.CharField(
        initial = "aaa\nbbb\nccc",
        required=True,
        widget = forms.Textarea(attrs={
            'placeholder': "aaa\nbbb\nccc", 
            "onchange" : "set_text(this.id)"
        }),
    )

class NormalDataTypeForm_Number(forms.Form):
    number_min = forms.IntegerField(
        initial = 1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_number_min(this.id)"
        })
    )
    number_max = forms.IntegerField(
        initial = 10,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_number_max(this.id)"
        })
    )
    number_step = forms.IntegerField(
        initial = 1,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_number_step(this.id)"
        })
    )

class NormalDataTypeForm_Date(forms.Form):
    import datetime
    date_min = forms.DateField(
        label='最小日付',
        required=True,        
        initial = datetime.date.today().strftime("%Y/%m/%d"),
        widget=forms.DateInput(attrs={
            "onchange" : "set_date_min(this.id)"
        })
    )
    date_max = forms.DateField(
        label='最大日付',
        required=True,        
        initial = (datetime.date.today() + datetime.timedelta(days=10)).strftime("%Y/%m/%d"),
        widget=forms.DateInput(attrs={
            "onchange" : "set_date_max(this.id)"
        })
    )
    date_step = forms.IntegerField(
        label='ステップ（日）',
        required=True,        
        initial = 1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_date_step(this.id)"
        })
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date_min = cleaned_data.get('date_min')
    #     date_max = cleaned_data.get('date_max')
    #     date_step = cleaned_data.get('date_step')

    #     if date_min is None or date_max is None or date_max is None:
    #         raise forms.ValidationError('フィールドが入力されていません。')

class NormalDataTypeForm_Datetime(forms.Form):
    import datetime
    datetime_min = forms.DateTimeField(
        label='最小日時',
        required=True,        
        initial = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:00"),
        widget=forms.DateTimeInput(attrs={
            "onchange" : "set_datetime_min(this.id)"
        })
    )
    datetime_max = forms.DateTimeField(
        label='最大日時',
        required=True,        
        initial = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y/%m/%d %H:%M:00"),
        widget=forms.DateTimeInput(attrs={
            "onchange" : "set_datetime_max(this.id)"
        })
    )
    datetime_step = forms.IntegerField(
        label='ステップ（秒）',
        required=True,        
        initial = 60,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_datetime_step(this.id)"
        })
    )

class LinkDataTypeForm_Text(forms.Form):
    
    text = forms.CharField(
        initial = "aaa\nbbb\nccc",
        required=True,
        widget = forms.Textarea(attrs={
            'placeholder': "aaa\nbbb\nccc", 
            "onchange" : "set_link_number_text(this.id)"
        }),
    )

class LinkDataTypeForm_Number(forms.Form):
    number_min = forms.IntegerField(
        initial = 1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_link_number_min(this.id)"
        })
    )
    number_max = forms.IntegerField(
        initial = 10,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_link_number_max(this.id)"
        })
    )
    number_step = forms.IntegerField(
        initial = 1,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_link_step(this.id)"
        })
    )

class LinkDataTypeForm_Date(forms.Form):
    import datetime
    date_min = forms.DateField(
        label='最小日付',
        required=True,        
        initial = datetime.date.today().strftime("%Y/%m/%d"),
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={
            "onchange" : "set_link_date_min(this.id)"
        })
    )
    date_max = forms.DateField(
        label='最大日付',
        required=True,        
        initial = (datetime.date.today() + datetime.timedelta(days=10)).strftime("%Y/%m/%d"),
        input_formats=['%Y/%m/%d'],
        widget=forms.DateInput(attrs={
            "onchange" : "set_link_date_max(this.id)"
        })
    )
    date_step = forms.IntegerField(
        label='ステップ（日）',
        required=True,        
        initial = 1,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_link_date_step(this.id)"
        })
    )

class LinkDataTypeForm_Datetime(forms.Form):
    import datetime
    datetime_min = forms.DateTimeField(
        label='最小日時',
        required=True,        
        initial = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:00"),
        widget=forms.DateTimeInput(attrs={
            "onchange" : "set_link_datetime_min(this.id)"
        })
    )
    datetime_max = forms.DateTimeField(
        label='最大日時',
        required=True,        
        initial = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y/%m/%d %H:%M:00"),
        widget=forms.DateTimeInput(attrs={
            "onchange" : "set_link_datetime_max(this.id)"
        })
    )
    datetime_step = forms.IntegerField(
        label='ステップ（秒）',
        required=True,        
        initial = 60,
        min_value=1,
        widget=forms.NumberInput(attrs={
            "onchange" : "set_link_datetime_step(this.id)"
        })
    )
