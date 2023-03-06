from django.db import models

# Create your models here.
class CreateModel(models.Model):
    column_name = models.CharField(max_length=50, default = "AAA")
    column_type = models.TextField(
        verbose_name="項目タイプ", 
        choices=[("1", "項目作成"), ("2", "リンク項目作成")], 
        blank=False,
        default=("1", "項目作成")
    )
    generate_type = models.TextField(
        verbose_name="生成タイプ", 
        choices=[("1", "組み合わせ"), ("2", "ランダム")], 
        blank=False,
        default=("1", "組み合わせ")
    )
    link_column_name = models.CharField(max_length=50, default = "AAA")
    data_type = models.TextField(
        verbose_name="データタイプ", 
        choices=[
            ("1", "文字"), 
            ("2", "数値"),
            ("3", "日付"), 
            ("4", "日時")
        ], 
        blank=False,
        default=("3", "日付")
    )

