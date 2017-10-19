function showdata(data1,data2){
    var myChart = echarts.init(document.getElementById('city'));

var colors = ['#5793f3', '#d14a61', '#675bba'];

var option = {
    color: colors,

    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        }
    },
    grid: {
        right: '10%'
    },
    toolbox: {
        feature: {
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
        }
    },
    legend: {
        data:['数据量']
    },
    xAxis: [
        {
            type: 'category',
            axisTick: {
                alignWithLabel: true
            },
            data: data1
        }
    ],
    yAxis: [
        {
            type: 'value',
            name: '数据量',
            min: 2000000,
            max: 30000000,
            position: 'right',
            axisLine: {
                lineStyle: {
                    color: colors[0]
                }
            },
            axisLabel: {
                formatter: '{value} '
            }
        },


    ],
    series: [
        {
            name:'数据量',
            type:'bar',
            data:data2
        }

    ]
};
myChart.setOption(option);

}
