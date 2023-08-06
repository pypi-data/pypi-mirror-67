# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foxcross']

package_data = \
{'': ['*'], 'foxcross': ['templates/*']}

install_requires = \
['aiofiles>=0.5.0,<0.6.0',
 'jinja2>=2.10,<3.0',
 'python-slugify[unidecode]>=4.0,<5.0',
 'starlette>=0.13.0,<0.14.0',
 'uvicorn>=0.11.0,<0.12.0']

extras_require = \
{'modin': ['modin>=0.7.0,<0.8.0'],
 'pandas': ['pandas>=1.0.0,<2.0.0'],
 'ujson': ['ujson>=2.0,<3.0']}

setup_kwargs = {
    'name': 'foxcross',
    'version': '0.10.0',
    'description': 'AsyncIO serving for data science models',
    'long_description': '# Foxcross\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/laactech/foxcross/blob/master/LICENSE.md)\n[![Build Status](https://travis-ci.org/laactech/foxcross.svg?branch=master)](https://travis-ci.org/laactech/foxcross)\n[![Build status](https://ci.appveyor.com/api/projects/status/github/laactech/foxcross?branch=master&svg=true)](https://ci.appveyor.com/project/laactech/foxcross)\n[![PyPI](https://img.shields.io/pypi/v/foxcross.svg?color=blue)](https://pypi.org/project/foxcross/)\n[![codecov](https://codecov.io/gh/laactech/foxcross/branch/master/graph/badge.svg)](https://codecov.io/gh/laactech/foxcross)\n\nAsyncIO serving for data science models built on [Starlette](https://www.starlette.io/)\n\n**Requirements**: Python 3.6.1+\n\n## Quick Start\nInstallation using `pip`:\n```bash\npip install foxcross\n```\n\nCreate some test data and a simple model in the same directory to be served:\n\ndirectory structure\n```\n.\n+-- data.json\n+-- models.py\n```\ndata.json\n```json\n[1,2,3,4,5]\n```\nmodels.py\n```python\nfrom foxcross.serving import ModelServing, run_model_serving\n\nclass AddOneModel(ModelServing):\n    test_data_path = "data.json"\n\n    def predict(self, data):\n        return [x + 1 for x in data]\n\nif __name__ == "__main__":\n    run_model_serving()\n```\n\nRun the model locally\n```bash\npython models.py\n```\n\nNavigate to `localhost:8000/predict-test/` in your web browser, and you should see the\nlist incremented by 1. You can visit `localhost:8000/` to see all the available\nendpoints for your model.\n\n## Why does this package exist?\nCurrently, some of the most popular data science model building frameworks such as PyTorch\nand Scikit-Learn do not come with a built in serving library similar to TensorFlow Serving.\n\nTo fill this gap, people create Flask applications to serve their model. This can be error\nprone, and the implementation can differ between each model. Additionally, Flask is a\n[WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)\nweb framework whereas Foxcross is built on [Starlette](https://www.starlette.io/), a\nmore performant [ASGI](https://asgi.readthedocs.io/en/latest/) web framework.\n\nFoxcross aims to be the serving library for data science models built with frameworks\nthat do not come with their own serving library. Using Foxcross enables consistent\nand testable serving of data science models.\n\n## Security\n\nIf you believe you\'ve found a bug with security implications, please do not disclose this\nissue in a public forum.\n\nEmail us at [support@laac.dev](mailto:support@laac.dev)\n',
    'author': 'Steven Pate',
    'author_email': 'steven@laac.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/laactech/foxcross',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
