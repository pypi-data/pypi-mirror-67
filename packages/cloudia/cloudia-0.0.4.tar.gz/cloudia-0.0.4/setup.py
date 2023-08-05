# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudia']

package_data = \
{'': ['*']}

install_requires = \
['japanize_matplotlib',
 'matplotlib',
 'nagisa',
 'pandas',
 'wordcloud',
 'wurlitzer']

entry_points = \
{'console_scripts': ['my-script = cloudia:main']}

setup_kwargs = {
    'name': 'cloudia',
    'version': '0.0.4',
    'description': 'Tools to easily create a word cloud',
    'long_description': '# Cloudia\nTools to easily create a word cloud.\n\n### from string\n```\nfrom cloudia import Cloudia\n\ntext = "text data"\nCloudia(text).plot()\n```\n\n![sample_img](https://github.com/vaaaaanquish/cloudia/blob/021a6d151fb6a3b579dc96b7086356fc0c225852/examples/img/sample_img.png?raw=true, "sample_img")\n  \nfrom : [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/)\n\n\n### from pandas\n```\ndf = pd.DataFrame({\'wc1\': [\'sample1\',\'sample2\'], \'wc2\': [\'hoge hoge piyo piyo fuga\', \'hoge\']})\n\n# plot from df\nCloudia(df).plot()\n\n# add df method\ndf.wc.plot(dark_theme=True)\n```\n\n![pandas_img](https://github.com/vaaaaanquish/cloudia/blob/021a6d151fb6a3b579dc96b7086356fc0c225852/examples/img/pandas_img.png?raw=true, "pandas_img")\n![dark_img](https://github.com/vaaaaanquish/cloudia/blob/021a6d151fb6a3b579dc96b7086356fc0c225852/examples/img/dark_img.png?raw=true, "dark_img")\n  \nfrom pandas.DataFrame or pandas.Series.\n\n\n### from japanese\n```\ntext = "これはCloudiaのテストです。WordCloudをつくるには本来、形態素解析の導入が必要になります。Cloudiaはmecabのような形態素解析器の導入は必要はなくnagisaを利用した動的な生成を行う事ができます。nagisaとjapanize-matplotlibは、形態素解析を必要としてきたWordCloud生成に対して、Cloudiaに対して大きく貢献しました。ここに感謝の意を述べたいと思います。"\n\nCloudia(text).plot()\n```\n\n![japanese_img](https://github.com/vaaaaanquish/cloudia/blob/021a6d151fb6a3b579dc96b7086356fc0c225852/examples/img/japanese_img.png?raw=true, "jap_img")\n  \nfrom japanese without morphological analysis module\n\n\n# Require\n\nI\'m waiting for this [PR](https://github.com/uehara1414/japanize-matplotlib/pull/9).\n```\npip install git+https://github.com/vaaaaanquish/japanize-matplotlib\n```\n\n# Install\n\n```\npip install cloudia\n```\n\n# Thanks\n\n- [japanize-matplotlib](https://github.com/uehara1414/japanize-matplotlib)\n- [nagisa](https://github.com/taishi-i/nagisa)\n',
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
