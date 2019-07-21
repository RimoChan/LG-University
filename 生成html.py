import os
import sys

import yaml
from jinja2 import Environment, FileSystemLoader

sys.path.append('d:/librian/librian本體')

import 導出文件


def 標題(文件名):
    return os.path.splitext(os.path.basename(文件名))[0]


with open('配置.yaml', encoding='utf8') as f:
    配置 = yaml.load(f)

文件列表 = [
    {'標題': 標題(文件名), '文件名': 文件名, 'html文件名': f'{標題(文件名)}.html'}
    for 文件名 in 配置['目录']
]

for i, 文件 in enumerate(文件列表):

    讀 = 導出文件.虛讀者(文件['文件名'], 簡化字=True)
    body內容 = 讀.body內容()

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./網頁/模板.html')
    s = template.render( 
        文件列表=文件列表,
        標題=文件['標題'], 
        body內容=body內容,
        前=文件列表[i-1] if i>0 else None,
        後=文件列表[i+1] if i<len(文件列表)-1 else None,
    )
    
    with open(f'./網頁/{文件["標題"]}.html', 'w', encoding='utf8') as f:
        f.write(s)
