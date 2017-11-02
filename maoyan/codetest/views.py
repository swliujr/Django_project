from django.shortcuts import render
from .code_test import CodeTest
from django.http import JsonResponse
# Create your views here.

def input_code(request):
    input_code = '''
y,m,d = map(str,'2017-10-09'.split('-'))
print(y,m,d)
'''
    return render(request, 'codetest/codetest.html', {'input_code': input_code}
                  )
def run(request):
    ct = CodeTest()
    item = {}
    input_code = request.POST['input_code']
    pyfile,py_code, code_run_result = ct.check_code_run(input_code)
    item['pyfile'] = pyfile
    item['input_code'] = py_code
    item['code_run_result'] = code_run_result
    return JsonResponse(item)
