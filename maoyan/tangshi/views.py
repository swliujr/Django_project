from django.shortcuts import render, HttpResponse
from SQLS.tangshi_sqls import TangShi


# Create your views here.
def poemers_search(request):
    if request.method == 'POST':
        poemer = request.POST['poemer']
        tangshi = TangShi()
        poemers_datas = tangshi.per_poemer_data(poemer)
        if not poemer:
            return HttpResponse('未输入诗人姓名')
        elif not poemers_datas:
            return HttpResponse('无此诗人数据')
        else:
            if tangshi.check_word_cloud(poemer):
                return render(request, 'tangshi/poemers_search.html',
                              {'poemers_datas': poemers_datas,
                               'poemer': poemer}
                              )
            else:
                tangshi.make_poemer_word_clound(poemer)
                return render(request, 'tangshi/poemers_search.html',
                              {'poemers_datas': poemers_datas,
                               'poemer': poemer}
                              )
    else:
        return HttpResponse('无数据')


def poemers(request):
    tangshi = TangShi()
    all_poemers_datas = tangshi.all_poemers_data()
    return render(request, 'tangshi/poemers.html',
                  {'all_poemers_datas': all_poemers_datas,
                   'poemer_alt': ''}
                  )


def all_word_cloud(request):
    tangshi = TangShi()
    all_poemers = tangshi.make_all_word_cloud()
    return render(request,'tangshi/all_poemers_words_cloud.html',{'all_poemers':all_poemers})
