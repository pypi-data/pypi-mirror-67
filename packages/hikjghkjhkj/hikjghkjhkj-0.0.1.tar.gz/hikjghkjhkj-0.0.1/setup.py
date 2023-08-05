from setuptools import find_packages, setup
setup(
    name='hikjghkjhkj',
    version='0.0.1',
    description='Python REST API client for Guacamole 0.9.13 version',
    author='unique',#作者
    author_email='896035629@qq.com',
    url="https://pypi.org/manage/projects/",
    #packages=find_packages(),
    packages=['main'],  #这里是所有代码所在的文件夹名称
    install_requires=['requests','numpy','pandas'],
)