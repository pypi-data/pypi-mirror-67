# coding=utf-8

from setuptools import setup, find_packages

# with open("README.md", "r",encoding='utf8') as fh:
#     long_description = fh.read()

setup(
    name='nb_log',  #
    version="0.2",
    description=(
        'very sharp display'
    ),
    # long_description=open('README.md', 'r',encoding='utf8').read(),
    long_description='very sharp display  and high-performance multiprocess safe roating file handler log',
    long_description_content_type="text/markdown",
    author='bfzs',
    author_email='909686719@qq.com',
    maintainer='ydf',
    maintainer_email='909686719@qq.com',
    license='BSD License',
    # packages=['douban'], #
    packages=find_packages(),
    # packages=['pikav1'], # 这样内层级文件夹的没有打包进去。
    include_package_data=True,
    platforms=["all"],
    url='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'eventlet==0.25.0',
        'gevent==1.4.0',
        'pymongo==3.5.1',
        'AMQPStorm==2.7.1',
        'pika==0.12.0',
        'rabbitpy==2.0.1',
        'decorator==4.4.0',
        'pysnooper==0.0.11',
        'Flask',
        'tomorrow3==1.1.0',
        'concurrent-log-handler==0.9.9',
        'redis',
        'persist-queue==0.4.2',
        'elasticsearch',
        'kafka-python==1.4.6',
        'requests',
        'gnsq==1.0.1',
        'psutil',
        'sqlalchemy==1.3.11',
        'sqlalchemy_utils==0.36.1',
        'apscheduler',
        'pikav0',
        'pikav1'
    ]
)
"""
打包上传
python setup.py sdist upload -r pypi
"""
