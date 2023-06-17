from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('index.html')


@app.route('/实习期分布.html')
def shixiqifenbu():
    return render_template('实习期分布.html')


@app.route('/出勤频率分布.html')
def chuqin():
    return render_template('出勤频率分布.html')


@app.route('/工资分布.html')
def money():
    return render_template('工资分布.html')


@app.route('/所属行业分布图.html')
def work_class():
    return render_template('所属行业分布图.html')


@app.route('/职位福利待遇.html')
def fu_li():
    return render_template('职位福利待遇.html')


@app.route('/wordcloud.html')
def wordcloud():
    return render_template('wordcloud.html')


if __name__ == '__main__':
    # 修改人：黄德攒   修改量：ALL_Project
    # 别再动代码了！球球各位姐姐了！！！

    # 实际部署不可以debug！！！
    # 通过url_map可以查看整个flask中的路由信息，已经注释，需要的时候再启用检查
    # print(app.url_map)
    app.run(host="127.0.0.1", port=5000, debug=True)
