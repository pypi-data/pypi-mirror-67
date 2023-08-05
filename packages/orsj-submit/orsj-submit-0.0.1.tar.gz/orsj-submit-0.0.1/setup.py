# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orsj_submit', 'orsj_submit.orsj']

package_data = \
{'': ['*'],
 'orsj_submit.orsj': ['static/*',
                      'static/content/*',
                      'static/fonts/*',
                      'static/scripts/*',
                      'templates/*']}

install_requires = \
['flask>=1.1.2,<2.0.0',
 'gunicorn>=20.0.4,<21.0.0',
 'pdfformfiller>=0.4,<0.5',
 'pyjade>=4.0.0,<5.0.0',
 'pypdf2>=1.26.0,<2.0.0',
 'pyyaml>=5.3.1,<6.0.0',
 'redis>=3.4.1,<4.0.0']

entry_points = \
{'console_scripts': ['orsj-submit = orsj_submit:main']}

setup_kwargs = {
    'name': 'orsj-submit',
    'version': '0.0.1',
    'description': "Web application of 'submitting papers' in ORSJ.",
    'long_description': 'Web application of "submitting papers" in ORSJ.\n\nORSJ: The Operations Research Society of Japan\nhttp://www.orsj.or.jp/\n\nOS: mac, ubuntu',
    'author': 'SaitoTsutomu',
    'author_email': 'tsutomu7@hotmail.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SaitoTsutomu/orsj-submit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
