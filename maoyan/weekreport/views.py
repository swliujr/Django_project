from django.shortcuts import render,HttpResponseRedirect
from SQLS.weekreport_sqls import WeekReport
from django.http import JsonResponse, HttpResponse


# Create your views here.

def add_report(request):
    if request.method == 'POST':
        wk = WeekReport()
        content = request.POST['content']
        create_time = request.POST['create_time']
        if not create_time:
            return HttpResponse('时间未选择,不能保存!')
        finished_status = request.POST['finished_status']
        cooperation = request.POST['cooperation']
        args = (content, create_time, finished_status, cooperation)
        alert_text = wk.add_report(args)
        return HttpResponse(alert_text)
    else:
        return HttpResponse('增加失败')

def update_report(request):
    if request.method == 'POST':
        wk = WeekReport()
        item = {}
        id = request.POST['id']
        content = request.POST['content']
        create_time = request.POST['create_time']
        finished_status = request.POST['finished_status']
        cooperation = request.POST['cooperation']
        item['id'] = id
        item['content'] = content
        item['create_time'] = create_time
        item['finished_status'] = finished_status
        item['cooperation'] = cooperation
        alter_text = wk.update_report(item)
        return HttpResponse(alter_text)
    else:
        return HttpResponse('更新失败')

def delete_report(request):
    wk = WeekReport()
    alter_text = wk.delete_report()
    return HttpResponse(alter_text)

#导出全部
def export_all_excel(request):
    wk = WeekReport()
    alert_text = wk.export_excel()
    return HttpResponse(alert_text)


def reports(request):
    wk = WeekReport()
    week_reports_data = wk.reports()
    max_id = len(week_reports_data) + 1
    return render(request, 'weekreport/weekreports.html',
                  {'week_reports_data': week_reports_data,
                   'max_id': max_id
                   }
)
