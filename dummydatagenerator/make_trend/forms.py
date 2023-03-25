from django import forms

class DocumentForm(forms.Form):

    document = forms.FileField(
        label = "CSVをアップロード",
        widget=forms.FileInput(attrs={
            "class" : "form-control"
        })
    )

slope_tooltip_msg = """0以上の実数を指定
倍率 > 1 -> 右肩上がり
倍率 = 1 -> 変化なし
倍率 < 1 -> 右肩下がり 
"""

amplitude_tooltip_msg = """1以上の実数を指定
変動率が大きいほど、増減値（波の高さ）が大きくなります。
変動率 = 1 -> 変化なし
"""

frequency_tooltip_msg = """実数を指定
値が大きいほど、激しく変動します。
周期 = 0 -> 変化なし
"""

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
        label = "倍率",
        widget=forms.NumberInput(attrs={
            "data-toggle" : "tooltip",
            "data-placement" : "auto",
            "title" : slope_tooltip_msg
        })
    )

    amplitude = forms.FloatField(
        initial = 2,
        min_value=1,
        label = "変動率",
        widget=forms.NumberInput(attrs={
            "data-toggle" : "tooltip",
            "data-placement" : "auto",
            "title" : amplitude_tooltip_msg,
        })
    )

    frequency = forms.FloatField(
        initial = 2.5,
        label = "周期",
        widget=forms.NumberInput(attrs={
            "data-toggle" : "tooltip",
            "data-placement" : "auto",
            "title" : frequency_tooltip_msg
        })
    )