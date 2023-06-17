from flask import Flask
# import gc

app = Flask(__name__)
# 生命周期上下文预处理
actx = app.app_context()
# 跳进坑里面
actx.push()
# 被人捞出来
actx.pop()
# 用完就要丢进垃圾桶！
# gc.collect()

# rctx = app.request_context()
# rctx.push()
# rctx.pop()
