# Named Entity Segmentation

## 简介

本项目是字符串令牌流分割库；
neseg -n 中国北京市联想科技有限公司 -d dict

### 功能

- 字符串令牌解析； 
- 支持令牌流；
- 解析器可以是自定义字典机械分割，每个token一个独立字典；
- 解析器也可以是正则表达式；
- 分割分正向和反向，都是从头开始；
- 生成对应令牌名称和解析出来的字符创元组，最后剩下的归为一组；

### 应用场景

- 各种名称的解析，如中文机构名、药品名称、地址的分割标注；

### TODO

- 设计参考re.scanner；
- 可以用生成器yield来做技术实现；
- 程序返回元组列表；

## 模块开发

### 本地

docker环境

    docker run -it --rm --name my-running-script \
        -v "$PWD":/usr/src/myapp \
        -w /usr/src/myapp \
        python:3 bash

常用指令

    python setup.py sdist       #构建源码分发包，Windows下为zip，Linux下为tag.gz
    python setup.py bdist       #构建二进制分发包
    python setup.py bdist_egg   #构建一个egg分发包，经常用来替代基于bdist生成的模式
    python setup.py build       #模块编译，构建安装时所需的所有内容
    python setup.py install     #模块安装，安装包到系统环境中
    python setup.py develop     #以开发方式安装包，不会真正的安装包，是在系统环境中创建一个软链接,便于调试

    easy_install ./dist/neseg-0.7-py3.8.egg  # 从本地的 .egg 文件安装
    easy_install <sdist>

    del D:\Anaconda3\envs\ner\lib\site-packages\neseg #模块卸载 - 手动删除 

### pypi发布

如果要发布自己的包，需要先到 pypi 上注册账号。

然后创建 ~/.pypirc 文件，此文件中配置 PyPI 访问地址和账号。

典型的 .pypirc 文件

    [distutils]
    index-servers = pypi

    [pypi]
    username:xxx
    password:xxx

然后使用这条命令进行信息注册，完成后，你可以在 PyPi 上看到项目信息。

    python setup.py register

    docker cp ~/.pypirc my-running-script:/root/
    docker run -it --rm --name my-running-script \
        -v "$PWD":/usr/src/myapp \
        -v ~/.pypirc:/root/.pypirc \
        -w /usr/src/myapp \
        python:3 python setup.py register

注册完了后，你还要上传源码包，别人才使用下载安装

    python setup.py sdist upload

    OR

    python setup.py sdist
    twine upload ./dist/neseg-0.7.tar.gz

## 附录 - 源码文件说明

    neseg
        /lib
            FMM.py  正向切词
            RMM.py  反向切词
        seg.py      
        main.py   主程序：无界面,参数命令行
    changelog.md    软件更新日志
    readme.md       软件使用、安装指南
