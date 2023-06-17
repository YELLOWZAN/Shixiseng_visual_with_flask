from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 25, 30, 18, 65, 70])
    .set_global_opts(title_opts=opts.TitleOpts(title="价格对比图", subtitle="各类商品价格对比"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)
try:
    bar.render(r'.\templates\index.html')
    print("页面生成成功")
except IndexError:
    print("data error!")
