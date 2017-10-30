from django.shortcuts import render, HttpResponse
from SQLS.tangshi_sqls import TangShi
import json


# Create your views here.
def poemers_search(request):
    if request.method == 'POST':
        poemer = request.POST['poemer']
        print(poemer)
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
#导出全部
def export_all_excel(request):
    tangshi = TangShi()
    alert_text = tangshi.export_excel(None)
    return HttpResponse(alert_text)

def export_per_excel(request):
    poemer = request.POST['poemer']
    print('xxxxx',poemer)
    tangshi = TangShi()
    poemers_datas = tangshi.per_poemer_data(poemer)
    print(poemers_datas)
    if not poemer:
        return HttpResponse('未输入诗人姓名 导出失败')
    elif not poemers_datas:
        return HttpResponse('无此诗人数据')
    else:
        alert_text = tangshi.export_excel(poemer)
    # else:
        return HttpResponse(alert_text)


def all_word_cloud(request):
    tangshi = TangShi()
    all_poemers = tangshi.make_all_word_cloud()
    # return render(request, 'tangshi/all_poemers_words_cloud.html', {'all_poemers': all_poemers})
    return HttpResponse(json.dumps(all_poemers), content_type='application/json')
    # return render(request, 'tangshi/return_ciyun.html', {'all_poemers': json.dumps(all_poemers)})


def poem_ajax(request):
    tangshi = TangShi()
    all_poemers_datas = tangshi.all_poemers_data()
    pages_tuple = divmod(len(all_poemers_datas), 16)
    if pages_tuple[1] != 0:
        pages = pages_tuple[0] + 1
    else:
        pages = pages_tuple[0]
    item = {}
    for page in range(1,pages+1):
        start = (page - 1) * 16
        end = page * 16
        item[page] = all_poemers_datas[start:end]
    print(item)
    return HttpResponse(json.dumps(item[2]))


