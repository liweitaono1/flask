from flask import Blueprint

# 1. 创建蓝图
admin_blu = Blueprint("admin", __name__, url_prefix="/admin")

# 蓝图也可以设置请求钩子, 只会监听该蓝图注册的路由(app的请求钩子会监听所有的请求)
@admin_blu.before_request
def check_superuser_login():  # 检查后台登录情况
    is_admin = session.get("is_admin")
    if not is_admin and not request.url.endswith("admin/login"):  # 如果管理员未登录 并且 不是访问的后台登录页面
        return redirect(url_for("home.index"))


# 4. 关联视图函数(避免循环导入)
from .views import *