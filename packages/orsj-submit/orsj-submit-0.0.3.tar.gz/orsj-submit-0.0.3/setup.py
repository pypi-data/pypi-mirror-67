# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orsj_submit', 'orsj_submit.orsj']

package_data = \
{'': ['*'],
 'orsj_submit.orsj': ['static/content/*',
                      'static/fonts/*',
                      'static/pdf/*',
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
    'version': '0.0.3',
    'description': "Web application of 'submitting papers' in ORSJ.",
    'long_description': '## Description\n\nWeb application of "submitting papers" in ORSJ.\n\nORSJ: The Operations Research Society of Japan\n\nhttp://www.orsj.or.jp/\n\n## OS\n\nmac, ubuntu\n\n## Usage\n\n### Step 1\n\nCopy setting file.\n\n```\n$ orsj-submit setting\n```\n\n### Step 2\n\nModify setting file.\n\n```\n$ edit setting.yml\n```\n\n### Step 3\n\nStart redis server.\n\n```\n$ orsj-submit redis\n```\n\n### Step 4\n\nIn annother shell, set environment.\n\n```\n$ export MAIL_USER=XXX\n$ export MAIL_PASSWD=XXX\n$ export SECRET_KEY=XXX\n```\n\n### Step 5\n\nstart web application.\n\n```\n$ orsj-submit run\n```\n\n## Using docker\n\nMust modify setting.yml & start_cmd of orsj.tgz.\n\n```bash\nwget -qO- <URL of orsj.tgz> | tar zxf -\ndocker run -d -u root -p 80:80 -e MAIL_USER=XXX -e MAIL_PASSWD=XXX -e SECRET_KEY=XXX \\\n  -v $PWD/orsj:/orsj -w /orsj --name orsj tsutomu7/scientific-python ash start_cmd\n```\n',
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
