function showdata(div_id,text,legend_data,series_data) {

    var myChart = echarts.init(document.getElementById(div_id));
var option = {
    title : {
        text: text,
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: legend_data
    },
    series : [
        {
            name: '分布个数',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            // data:[
            //     {value:335, name:'直接访问'},
            //     {value:310, name:'邮件营销'},
            //     {value:234, name:'联盟广告'},
            //     {value:135, name:'视频广告'},
            //     {value:1548, name:'搜索引擎'}
            // ],
             data:series_data,
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

    myChart.setOption(option);

};
