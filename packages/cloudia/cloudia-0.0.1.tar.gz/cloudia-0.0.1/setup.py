# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudia']

package_data = \
{'': ['*']}

install_requires = \
['japanize_matplotlib', 'matplotlib', 'nagisa', 'pandas', 'wordcloud']

entry_points = \
{'console_scripts': ['my-script = cloudia:main']}

setup_kwargs = {
    'name': 'cloudia',
    'version': '0.0.1',
    'description': 'Tools to easily create a word cloud',
    'long_description': "# Cloudia\nTools to easily create a word cloud.\n\n\n# Require\n\nI'm waiting for this [PR](https://github.com/uehara1414/japanize-matplotlib/pull/9).\n```\npip install git+https://github.com/vaaaaanquish/japanize-matplotlib\n```\n\n# Install\n\n```\npip install cloudia\n```\n",
    'author': 'vaaaaanquish',
    'author_email': '6syun9@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vaaaaanquish/cloudia',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
