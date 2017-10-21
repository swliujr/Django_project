function showdata(div_id,text,legend_data,yAxis_data,series_data) {
    var myChart = echarts.init(document.getElementById(div_id));
    var option = {
        title: {
            text: text
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: legend_data
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        yAxis: {
            type: 'category',
            data: yAxis_data
        },
        series: series_data
    };
    myChart.setOption(option);

};
