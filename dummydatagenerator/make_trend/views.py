from django.shortcuts import render
from .forms import *
from .make_trend import makeTrend
from .graph import Plot_Graph
from django.http import HttpResponse

CSV_TEXT = ""
OUTPUT_DF = None
VIEW_TABLE_THRESHOLD = 5

# Create your views here.
def make_trend(request):
    global CSV_TEXT, OUTPUT_DF
    if request.method == 'POST':
        if "upload_csv" in request.POST:
            CSV_TEXT = request.FILES["document"].read().decode('utf-8')
            make_trend = makeTrend()
            try:
                make_trend.read_from_csvtext(CSV_TEXT)
            except:
                return render(request, "make_trend.html", {
                    "forms" : DocumentForm(request.POST),
                    "input_df" : "",
                    "error_msg" : "CSVの形式になっていない可能性があります。ファイルを確認してください。",
                })
            return render(request, "make_trend.html", {
                "forms" : DocumentForm(request.POST),
                "input_df" : make_trend.input_df.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                "error_msg" : "",
                "trendforms" : TrendForm()
            })
        elif "set_trend" in request.POST:
            make_trend = makeTrend()
            try:
                make_trend.read_from_csvtext(CSV_TEXT)
            except:
                return render(request, "make_trend.html", {
                    "forms" : DocumentForm(request.POST),
                    "input_df" : "",
                    "error_msg" : make_trend.error_msg_dict["error_msg"],
                })
            make_trend.trend_x(request.POST["base_column"], request.POST["target_column"], float(request.POST["slope"]))
            make_trend.trend_sinx(request.POST["base_column"], request.POST["target_column"], float(request.POST["amplitude"]), float(request.POST["frequency"]))
            if (make_trend.error_code == 1): 
                return render(request, "make_trend.html", {
                    "forms" : DocumentForm(request.POST),
                    "input_df" : make_trend.input_df.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                    "error_msg_trendform" : make_trend.error_msg_dict["error_msg"],
                    "trendforms" : TrendForm(request.POST)
                })

            x_in = make_trend.input_df.groupby(request.POST["base_column"]).mean(numeric_only=True).index
            y_in = make_trend.input_df.groupby(request.POST["base_column"]).mean(numeric_only=True)[request.POST["target_column"]]
            x_out = make_trend.output_df.groupby(request.POST["base_column"]).mean(numeric_only=True).index
            y_out = make_trend.output_df.groupby(request.POST["base_column"]).mean(numeric_only=True)[request.POST["target_column"]]
            # chart = None
            chart = Plot_Graph(
                x_in.to_list(), y_in.to_list(),
                x_out.to_list(), y_out.to_list(),
                request.POST["base_column"], request.POST["target_column"]
            )
            OUTPUT_DF = make_trend.output_df
            return render(request, "make_trend.html", {
                "forms" : DocumentForm(request.POST),
                "input_df" : make_trend.input_df.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                "error_msg_trendform" : "",
                "trendforms" : TrendForm(request.POST),
                "output_df" : make_trend.output_df.head(VIEW_TABLE_THRESHOLD).to_html(classes=["table", "table-bordered", "table-hover, overflow-scroll"]),
                "chart" : chart,
            })
        elif "download_csv" in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=filename.csv'
            OUTPUT_DF.to_csv(path_or_buf=response, sep=',', index=False)
            return response
    else:
        pass
    return render(request, "make_trend.html", {
        "forms" : DocumentForm(request.POST)
    })
