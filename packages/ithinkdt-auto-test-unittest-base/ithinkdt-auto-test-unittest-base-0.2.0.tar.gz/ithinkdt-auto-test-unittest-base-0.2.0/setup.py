# !usr/bin/env python
# _*_ coding: utf-8 _*_

from setuptools import setup
from setuptools import find_packages


setup(
    name='ithinkdt-auto-test-unittest-base',  # 项目代码所在目录，也是pip 要上传的项目名称
    version='0.2.0',  # 工具的版本号
    description='python auto test of basic page operations',
    long_description='python libs of basic page operations',
    license='MIT',
    author='huiLi',
    author_email='lihui@ithinkdt.com',
    packages=find_packages(where='./ithinkdt-auto-test-unittest-base'),  # 查找包的路径
    package_dir={'': 'ithinkdt-auto-test-unittest-base'},      # 包的root 路径映射到的实际路径
    install_requires=['selenium'],
    platforms='any'
)
