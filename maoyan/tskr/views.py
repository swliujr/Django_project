from django.shortcuts import render
from django.db.models import Count
from SQLS.tskr_sqls import TsKr


# Create your views here.




def tskr_tu(request):
    json_legend_data, json_series_data = TsKr().kr_pie()
    total_words_json_yAxis_data, total_words_json_series_data = TsKr().total_words_top()
    favorite_json_yAxis_data, favorite_json_series_data = TsKr().favorite_top()
    title_pv_json_yAxis_data, title_pv_json_series_data = TsKr().title_pv_top()

    return render(request, 'tskr/36kr_tu.html', {'json_legend_data': json_legend_data,
                                                 'json_series_data': json_series_data,

                                                 'total_words_json_yAxis_data': total_words_json_yAxis_data,
                                                 'total_words_json_series_data': total_words_json_series_data,
                                                 'favorite_json_yAxis_data': favorite_json_yAxis_data,
                                                 'favorite_json_series_data': favorite_json_series_data,
                                                 'title_pv_json_yAxis_data': title_pv_json_yAxis_data,
                                                 'title_pv_json_series_data': title_pv_json_series_data

                                                 })
