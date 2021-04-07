import os
import sys


def get_path():
    """获取项目根目录
    :return: base_path 项目根目录
    """
    # 判断运行环境（打包后的环境运行，还是本地环境）
    # 若为打包后运行环境，用该方法获取项目路径
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    # 若为本地运行环境，用该方法获取项目路径
    elif __file__:
        # os.path.dirname（）去掉文件名，返回目录
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    else:
        base_path = None
    return base_path


BASE_DIR = None
if not BASE_DIR:
    BASE_DIR = get_path()
