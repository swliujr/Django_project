#coding:utf8
import os
from os import path
import json
import xlsxwriter
from .get_mysql_data import Get_Mysql_data
from maoyan.settings import BASE_DIR


class WeekReport(Get_Mysql_data):
    def __init__(self):
        super(WeekReport, self).__init__()
        # 各年份电影数量饼图
        self.show_weekreport_sql = '''
select @i:=@i+1 as id,a.*
from (
select content,substr(create_time,1,10) as create_time,finished_status,cooperation
from local_db.weekreport
where create_time>=SUBDATE(CURRENT_DATE,DATE_FORMAT(CURRENT_DATE,'%w')-1) and create_time<=SUBDATE(CURRENT_DATE,DATE_FORMAT(CURRENT_DATE,'%w')-5)
order by  create_time
) as a,(select @i:=0) as it
'''
        self.update_report_sql = '''
        update local_db.weekreport set content='{}',create_time='{}',finished_status='{}', cooperation='{}' where id={}
'''
        self.detele_sql = 'truncate table local_db.weekreport'

    def add_report(self, args):
        sql = 'insert into local_db.weekreport(content,create_time,finished_status,cooperation) values(%s,%s,%s,%s)'
        alert_text = self.insert_data(sql, args)
        return alert_text

    def update_report(self, item):
        content = item['content']
        create_time = item['create_time']
        finished_status = item['finished_status']
        cooperation = item['cooperation']
        id = item['id']
        sql = self.update_report_sql.format(content, create_time, finished_status, cooperation, id)
        self.exesql(sql)
        return '更新成功!'

    def delete_report(self):
        self.exesql(self.detele_sql)
        return '数据表全部清空'


    def reports(self):
        week_reports_data = []
        datas = self.fetch_data(self.show_weekreport_sql)
        fields = ['id', 'content', 'create_time', 'finished_status', 'cooperation']
        for data in datas:
            item = {}
            for i in range(len(data)):
                if i == 0:
                    item[fields[i]] = int(data[i])
                else:
                    item[fields[i]] = data[i]
            week_reports_data.append(item)
        return week_reports_data

    def export_excel(self):
        par_path = path.join(path.dirname(path.dirname(BASE_DIR)), '1-week')
        os.chdir(par_path)
        data = self.reports()
        base_file = '数据仓库-程鑫垚周报({}).xlsx'
        file_name = ''.join(data[-1]['create_time'].split('-'))
        file = base_file.format(file_name)
        if os.path.isfile(file):
            os.remove(file)
        if data:
            fields =['id', 'content', 'create_time', 'finished_status', 'cooperation']
            field_dict = {'id':'序号', 'content':'工作内容', 'create_time':'完成时间', 'finished_status':'完成情况', 'cooperation':'协同部门/人'}
            workbook = xlsxwriter.Workbook(file)
            worksheet = workbook.add_worksheet('data')
            # 表头格式
            format1 = workbook.add_format(
                {'bold': True, 'font_color': 'black', 'font_size': 10, 'align': 'left', 'font_name': '宋体','border':1})
            # 除日期A列外数值区域
            format2 = workbook.add_format({'font_color': 'black', 'font_size': 9, 'align': 'left', 'font_name': '宋体','border':1})
            #设置行宽
            worksheet.set_row(0, 30)
            worksheet.set_row(1, 15)
            # A列列宽设置能更好的显示
            worksheet.set_column("A:A", 4)
            worksheet.set_column('B:B', 30)
            worksheet.set_column('C:C', 9)
            worksheet.set_column('D:D', 9)
            worksheet.set_column('E:E', 12)
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': 'white'}
            )
            begin_md = data[0]['create_time'].split('-')[1] + '月' + data[0]['create_time'].split('-')[2] + '日'
            end_md = data[-1]['create_time'].split('-')[1] + '月' + data[-1]['create_time'].split('-')[2] + '日'
            merge_content = '星河金服数据开发周报{}--{}'.format(begin_md, end_md)
            worksheet.merge_range('A1:E1', merge_content, merge_format)  # 合并A1-Q2的矩阵魏一个单元格
            # 插入第一行表头标题
            for i in range(0, len(fields)):
                field = fields[i]
                worksheet.write(1, i, field_dict[field], format1)
            for i in range(len(data)):
                item = data[i]
                for j in range(len(fields)):
                    field = fields[j]
                    worksheet.write(i+2, j, item[field], format2)
            workbook.close()
            alert_text = '导出%s条数据到excel成功' % len(data)
        else:
            alert_text = '无数据 导出失败'
        return alert_text

