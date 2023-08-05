# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_error_skins', 'django_error_skins.migrations']

package_data = \
{'': ['*'],
 'django_error_skins': ['context_processors/*',
                        'static/allauth_skins/css/*',
                        'static/allauth_skins/images/*',
                        'static/allauth_skins/images/default/*',
                        'static/allauth_skins/js/*',
                        'static/allauth_skins/sass/*',
                        'static/allauth_skins/sass/abstracts/*',
                        'static/allauth_skins/sass/base/*',
                        'static/allauth_skins/sass/components/*',
                        'static/allauth_skins/sass/pages/*',
                        'templatetags/*']}

install_requires = \
['django-widget-tweaks>=1.4.8,<2.0.0']

setup_kwargs = {
    'name': 'django-error-skins',
    'version': '0.1.0',
    'description': 'Styled templates for django error pages',
    'long_description': '# Error Skins\n\nStyled templates for django-error\n',
    'author': 'Adin Hodovic',
    'author_email': 'hodovicadin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
