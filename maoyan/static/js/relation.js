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
              "value": 27

          }, {
              "name": "计算机科学与教育软件学院",
              "value": 1,
              "symbolSize": 9,
              "category": "计算机科学与教育软件学院",
              "draggable": "true"
          }, {
              "name": "地理科学学院",
              "value": 1,
              "symbolSize": 18,
              "category": "地理科学学院",
              "draggable": "true"
          }, {
              "name": "机械与电气工程学院",
              "value": 1,
              "symbolSize": 15,
              "category": "机械与电气工程学院",
              "draggable": "true"
          }, {
              "name": "经济与统计学院",
              "value": 1,
              "symbolSize": 18,
              "category": "经济与统计学院",
              "draggable": "true"
          }, {
              "name": "土木工程学院",
              "value": 1,
              "symbolSize": 24,
              "category": "土木工程学院",
              "draggable": "true"
          }, {
              "name": "新闻与传播学院",
              "value": 1,
              "symbolSize": 15,
              "category": "新闻与传播学院",
              "draggable": "true"
          }, {
              "name": "外国语学院",
              "value": 1,
              "symbolSize": 18,
              "category": "外国语学院",
              "draggable": "true"
          }, {
              "name": "人文学院",
              "value": 1,
              "symbolSize": 30,
              "category": "人文学院",
              "draggable": "true"
          },{
              "name": "数学与信息科学学院",
              "value": 1,
              "symbolSize": 18,
              "category": "数学与信息科学学院",
              "draggable": "true"
          },  {
              "name": "工商管理学院",
              "value": 1,
              "symbolSize": 18,
              "category": "工商管理学院",
              "draggable": "true"
          }, {
              "name": "法学院",
              "value": 1,
              "symbolSize": 6,
              "category": "法学院",
              "draggable": "true"
          }, {
              "name": "公共管理学院",
              "value": 1,
              "symbolSize": 9,
              "category": "公共管理学院",
              "draggable": "true"
          } ,{
              "name": "卫斯理安学院",
              "value": 1,
              "symbolSize": 6,
              "category": "卫斯理安学院",
              "draggable": "true"
          }, {
              "name": "政治与公民教育学院",
              "value": 1,
              "symbolSize": 3,
              "category": "政治与公民教育学院",
              "draggable": "true"
          },{
              "name": "旅游学院",
              "value": 1,
              "symbolSize": 12,
              "category": "旅游学院",
              "draggable": "true"
          }, {
              "name": "教育学院",
              "value": 1,
              "symbolSize": 18,
              "category": "教育学院",
              "draggable": "true"
          },  {
              "name": "环境科学与工程学院",
              "value": 1,
              "symbolSize": 6,
              "category": "环境科学与工程学院",
              "draggable": "true"
          },{
              "name": "化学化工学院",
              "value": 1,
              "symbolSize": 15,
              "category": "化学化工学院",
              "draggable": "true"
          }, {
              "name": "物理与电子工程学院",
              "value": 1,
              "symbolSize": 12,
              "category": "物理与电子工程学院",
              "draggable": "true"
          }, {
              "name": "建筑与城市规划学院",
              "value": 1,
              "symbolSize": 12,
              "category": "建筑与城市规划学院",
              "draggable": "true"
          },  {
              "name": "美术与设计学院",
              "value": 1,
              "symbolSize": 27,
              "category": "美术与设计学院",
              "draggable": "true"
          },  {
              "name": "生命科学学院",
              "value": 1,
              "symbolSize": 9,
              "category": "生命科学学院",
              "draggable": "true"
          }, {
              "name": "体育学院",
              "value": 1,
              "symbolSize": 6,
              "category": "体育学院",
              "draggable": "true"
          },  {
              "name": "音乐舞蹈学院",
              "value": 1,
              "symbolSize": 9,
              "category": "音乐舞蹈学院",
              "draggable": "true"
          }],
          links: [{
              "source": "广州大学",
              "target": "计算机科学与教育软件学院"
          },  {
              "source": "广州大学",
              "target": "地理科学学院"
          },  {
              "source": "广州大学",
              "target": "机械与电气工程学院"
          },{
              "source": "广州大学",
              "target": "经济与统计学院"
          }, {
              "source": "广州大学",
              "target": "土木工程学院"
          },{
              "source": "广州大学",
              "target": "新闻与传播学院"
          },{
              "source": "广州大学",
              "target": "外国语学院"
          },  {
              "source": "广州大学",
              "target": "人文学院"
          }, {
              "source": "广州大学",
              "target": "数学与信息科学学院"
          }, {
              "source": "广州大学",
              "target": "工商管理学院"
          },  {
              "source": "广州大学",
              "target": "法学院"
          },  {
              "source": "广州大学",
              "target": "公共管理学院"
          },   {
              "source": "广州大学",
              "target": "卫斯理安学院"
          },   {
              "source": "广州大学",
              "target": "政治与公民教育学院"
          }, {
              "source": "广州大学",
              "target": "旅游学院"
          },{
              "source": "广州大学",
              "target": "教育学院"
          },{
              "source": "广州大学",
              "target": "环境科学与工程学院"
          }, {
              "source": "广州大学",
              "target": "化学化工学院"
          },  {
              "source": "广州大学",
              "target": "物理与电子工程学院"
          }, {
              "source": "广州大学",
              "target": "建筑与城市规划学院"
          }, {
              "source": "广州大学",
              "target": "美术与设计学院"
          },  {
              "source": "广州大学",
              "target": "生命科学学院"
          },   {
              "source": "广州大学",
              "target": "体育学院"
          }, {
              "source": "广州大学",
              "target": "音乐舞蹈学院"
          }],
          categories: [{
              'name': '计算机科学与教育软件学院'
          }, {
              'name': '地理科学学院'
          }, {
              'name': '机械与电气工程学院'
          }, {
              'name': '经济与统计学院'
          }, {
              'name': '土木工程学院'
          }, {
              'name': '新闻与传播学院'
          }, {
              'name': '外国语学院'
          }, {
              'name': '人文学院'
          }, {
              'name': '数学与信息科学学院'
          }, {
              'name': '工商管理学院'
          }, {
              'name': '法学院'
          }, {
              'name': '公共管理学院'
          }, {
              'name': '卫斯理安学院'
          }, {
              'name': '政治与公民教育学院'
          }, {
              'name': '旅游学院'
          }, {
              'name': '教育学院'
          }, {
              'name': '环境科学与工程学院'
          }, {
              'name': '化学化工学院'
          }, {
              'name': '物理与电子工程学院'
          }, {
              'name': '建筑与城市规划学院'
          }, {
              'name': '美术与设计学院'
          }, {
              'name': '生命科学学院'
          }, {
              'name': '体育学院'
          }, {
              'name': '音乐舞蹈学院'
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