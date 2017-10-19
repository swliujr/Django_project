function showdata(div_id,xAxis_data,series_data) {
    var myChart = echarts.init(document.getElementById(div_id));
    var option = {
    title: {
        text: '模型调用各时间段分布',

    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:['各时间段请求次数']
    },
    toolbox: {
        show: true,
        feature: {
            dataZoom: {
                yAxisIndex: 'none'
            },
            dataView: {readOnly: false},
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: xAxis_data
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value}次'
        }
    },
    series: [
        {
            name:'调用次数',
            type:'line',
            data:series_data,

        }
       ],

};

    myChart.setOption(option);

};
