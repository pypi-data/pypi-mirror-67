#from distutils.core import setup
from os import path as os_path
from setuptools import setup, find_packages

VERSION = '0.0.6'

tests_require = []

install_requires = []

this_directory = os_path.abspath(os_path.dirname(__file__))
# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(name='scrapy-random-fake-ua',
      url='https://github.com/zs527523251/scrapy-random-fake-ua',  # 项目包的地址
      author="zhousan",  # Pypi用户名称
      author_email='527523251@qq.com',  # Pypi用户的邮箱
      keywords='python pi',
      description='scrapy random fake useragent.',
      long_description_content_type="text/markdown",  # 指定包文档格式为markdown
      license='MIT',  # 开源许可证类型
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],

      version=VERSION,
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},

      entry_points={'nose.plugins': []},
      packages=find_packages(),
)
