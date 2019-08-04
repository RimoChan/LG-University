import sys

import yaml

sys.path.append('d:/librian/librian本體')
import 導出文件
sys.path.append('d:/閱讀器')
import 生成html


def body(文件名):
    讀 = 導出文件.虛讀者(文件名, 簡化字=True)
    return 讀.body內容()


with open('配置.yaml', encoding='utf8') as f:
    配置 = yaml.load(f)

生成html.生成html(body, 配置)
