# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['china_region_data']

package_data = \
{'': ['*']}

install_requires = \
['cached_property>=1.5.1,<2.0.0']

setup_kwargs = {
    'name': 'china-region-data',
    'version': '0.2.0',
    'description': '中国行政区域数据',
    'long_description': '# 中国行政区域数据\n\n根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。\n\n## install\n\n```bash\npip3 install china-region-data\n```\n\n## example\n\n```python\nfrom china_region_data import provinces, cities, counties, Region\n\n\n广东 = Region("广东省")\n深圳 = Region("深圳市")\n南山 = Region("南山区")\nassert 广东.name == "广东省"\nassert 广东.level == 1\n\nfor 广东城市 in 广东.subordinate:\n    assert 广东城市.level == 2\n\nassert 深圳.superior == 广东\nassert 南山.superior.superior == 广东\nassert 南山 in 南山.superior\nassert 南山 in 南山.superior.superior\nassert not Region("合肥市") in 广东\n```\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/china-region-data',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
