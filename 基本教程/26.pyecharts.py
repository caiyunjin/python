'''
Author: caiyunjin caiyunjin@vip.qq.com
Date: 2023-04-23 20:47:32
LastEditors: caiyunjin caiyunjin@vip.qq.com
LastEditTime: 2023-04-24 07:08:38
FilePath: \python\基本教程\26.pyecharts.py
Description: 
'''
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()
# x轴数据
line.add_xaxis(['中国', '美国', '韩国'])
# y轴数据
line.add_yaxis('GDP', [120, 132, 101])
# 标题设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title='GDP展示', pos_left='center', pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)


# 生成图像
line.render()
