from flask import Blueprint

# 1. 创建蓝图
user_blu = Blueprint("user", __name__, url_prefix="/user")

# 4. 关联视图函数(避免循环导入)
from .views import *