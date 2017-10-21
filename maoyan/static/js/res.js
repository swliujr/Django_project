function relation() {
    var myChart=echarts.init(document.getElementById('relation'));
    var option = {
    backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }]),
       title:{
        text: "关系图谱",
        subtext: "公司关系",
        top: "top",
        left: "center"
    },
      tooltip: {},
      legend: [{
          formatter: function (name) {
        return echarts.format.truncateText(name, 60, '18px Microsoft Yahei', '…');
    },
    tooltip: {
        show: true
    },
          selectedMode: 'false',
          bottom: 20,
          data: ['计算机科学与教育软件学院', '地理科学学院', '机械与电气工程学院', '经济与统计学院', '土木工程学院', '新闻与传播学院', '外国语学院', '人文学院', '数学与信息科学学院', '工商管理学院', '法学院', '公共管理学院', '卫斯理安学院', '政治与公民教育学院', '旅游学院', '教育学院', '环境科学与工程学院', '化学化工学院', '物理与电子工程学院', '建筑与城市规划学院', '美术与设计学院', '生命科学学院', '体育学院', '音乐舞蹈学院']
      }],
      toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: true},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
      animationDuration: 3000,
      animationEasingUpdate: 'quinticInOut',
      series: [{
          name: '广州大学',
          type: 'graph',
          layout: 'force',

          force: {
              repulsion: 50
          },
          data: [{
              "name": "广州大学",
              // "x": 0,
              // y: 0,
              "symbolSize": 20,
              "draggable": "true",
              "value":4

          }, {
              "name": "g1",
              "value": 1,
              "symbolSize": 9,
              "category": "g1",
              "draggable": "true"
          }, {
              "name": "g2",
              "value": 1,
              "symbolSize": 9,
              "category": "g2",
              "draggable": "true"
          }, {
              "name": "g3",
              "value": 1,
              "symbolSize": 9,
              "category": "g3",
              "draggable": "true"
          }, {
              "name": "g4",
              "value": 1,
              "symbolSize": 9,
              "category": "g4",
              "draggable": "true"
          }],
          links: [ {
              "source": "广州大学",
              "target": "g1"
          },  {
              "source": "广州大学",
              "target": "g2"
          },   {
              "source": "广州大学",
              "target": "g3"
          }, {
              "source": "广州大学",
              "target": "g4"
          }],
          categories: [{
              'name': 'g1'
          }, {
              'name': 'g2'
          }, {
              'name': 'g3'
          }, {
              'name': 'g4'
          }],
          focusNodeAdjacency: true,
          roam: true,
          label: {
              normal: {

                  show: true,
                  position: 'top',

              }
          },
          lineStyle: {
              normal: {
                  color: 'source',
                  curveness: 0,
                  type: "solid"
              }
          }
      }]
  };
    myChart.setOption(option);
}