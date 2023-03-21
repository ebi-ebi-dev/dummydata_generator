from django import forms

class DocumentForm(forms.Form):

    document = forms.FileField(
        label = "CSVをアップロード",
        widget=forms.FileInput(attrs={
            "class" : "form-control"
        })
    )

class TrendForm(forms.Form):

    base_column = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder':'項目名', 
        }),
        label = "軸となる項目名",
    )

    target_column = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder':'項目名', 
        }),
        label = "傾向を付与する数値型の項目名",
    )

    slope = forms.FloatField(
        initial = 1,
        min_value=0.1,
        widget=forms.NumberInput(attrs={
            
        })
    )

    amplitude = forms.FloatField(
        initial = 1,
        widget=forms.NumberInput(attrs={
            
        })
    )

    frequency = forms.IntegerField(
        initial = 32,
        min_value=1,
        widget=forms.NumberInput(attrs={
            
        })
    )