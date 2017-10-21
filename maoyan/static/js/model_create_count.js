function showdata(div_id,text,legend_data,xAxis_data,series_data) {

    var myChart = echarts.init(document.getElementById(div_id));
    var option = {
    title: {
        text: text,
        left:'center'

    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data:legend_data,
        show:false,
        right:'right'

    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },

    toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {}
            }

    },
    xAxis: {
        type: 'category',
        boundaryGap: true,
        data:xAxis_data
    },
    yAxis: {
        type: 'value'
    },
    series: series_data
};
    myChart.setOption(option);

};
