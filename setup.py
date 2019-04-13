from setuptools import setup, find_packages

setup(
    name = "china_stock_calendar",
    version = "0.0.1",
    packages = find_packages(),
    install_requires=[
        'requests'
    ],

    author="bond",
    author_email="zzdjavajob@163.com",
    description="The stock calendar for china",
    license="MIT",
    keywords="stock exchange for shenzhen , shanghai",
    url="https://github.com/zhouzhengde/china_stock_calendar.git",

    package_data={
        '': ['*.csv'],
    },
    entry_points={
        'console_scripts': [
        ]
    }
)
