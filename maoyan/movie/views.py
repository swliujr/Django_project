from django.shortcuts import render
from .models import Movie
from django.db.models import Count
from SQLS.movie_sqls import MovieTu


# Create your views here.

def show_movie(request):
    movie_datas = Movie.objects.all()
    return render(request, 'movie/show_movie.html', {'movie_datas': movie_datas})


def tu(request):
    json_legend_data, json_series_data = MovieTu().movie_pie()
    bar_json_xAxis_data, bar_json_series_data = MovieTu().movie_type_bar()
    piaofang_json_yAxis_data, piaofang_json_series_data = MovieTu().movie_piaofang_top()
    tosee_json_yAxis_data, tosee_json_series_data = MovieTu().movie_tosee_top()

    return render(request, 'movie/movie_tu.html', {'json_legend_data': json_legend_data,
                                                   'json_series_data': json_series_data,
                                                   'bar_json_xAxis_data': bar_json_xAxis_data,
                                                   'bar_json_series_data': bar_json_series_data,
                                                   'piaofang_json_yAxis_data': piaofang_json_yAxis_data,
                                                   'piaofang_json_series_data': piaofang_json_series_data,
                                                   'tosee_json_yAxis_data': tosee_json_yAxis_data,
                                                   'tosee_json_series_data': tosee_json_series_data,

                                                   })
