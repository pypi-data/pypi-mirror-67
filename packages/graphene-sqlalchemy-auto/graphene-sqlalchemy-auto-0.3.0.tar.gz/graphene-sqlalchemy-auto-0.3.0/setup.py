# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphene_sqlalchemy_auto']

package_data = \
{'': ['*']}

install_requires = \
['graphene-sqlalchemy>=2.3.0,<3.0.0']

setup_kwargs = {
    'name': 'graphene-sqlalchemy-auto',
    'version': '0.3.0',
    'description': 'generate default graphene schema from sqlalchemy model base on [graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy.git)\n',
    'long_description': 'generate default graphene schema from sqlalchemy model base on [graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy.git)\n\n# Installation\n\njust run\n```shell script\npip install graphene_sqlalchemy_auto\n```\n\n# How To Use\nexample :\n```python\nfrom graphene_sqlalchemy_auto import QueryObjectType,MutationObjectType\nfrom sqlalchemy.ext.declarative import declarative_base\nimport graphene\n\nBase = declarative_base() \n\nclass Query(QueryObjectType):\n    class Meta:\n        declarative_base = Base\n\n\nclass Mutation(MutationObjectType):\n    class Meta:\n        declarative_base = Base\n        \n        # include_object = [UserCreateMutation, UserUpdateMutation]\n\n\nschema = graphene.Schema(query=Query, mutation=Mutation)\n\n```\nnow you can use schema everywhere.some like flask,fastapi\nalso more example you can find in [example](https://github.com/goodking-bq/graphene-sqlalchemy-auto/tree/master/example)',
    'author': 'golden',
    'author_email': 'goodking_bq@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/goodking-bq/graphene-sqlalchemy-auto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
