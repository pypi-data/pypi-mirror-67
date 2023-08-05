# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mwdictionary']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.12.1,<0.13.0']

setup_kwargs = {
    'name': 'mwdictionary',
    'version': '0.1.2',
    'description': 'API Wrapper for the Merriam-Webster API.',
    'long_description': '# mwdictionary\n\nSmall wrapper around the Merriam-Webster API. Has both a sync and async interface thanks to [httpx](https://github.com/encode/httpx).\n\n## Installation\n\n`pip install mwdictionary`\n\n## Usage\n\nUsing mwdictionary\'s sync interface:\n\n```python\n>>> from mwdictionary import MWClient\n>>> client = MWClient(key="YOUR-KEY-HERE")\n>>> client.get("python")\nWord(word=\'python\', wordtype=\'noun\', shortdef=\'as in anaconda, boa\', synonyms=[\'adder\', \'anaconda\', \'asp\', \'black racer\', \'blacksnake\', \'blue racer\', \'boa\', \'bull snake\', \'bushmaster\', \'chicken snake\', \'cobra\', \'constrictor\', \'copperhead\', \'coral snake\', \'cottonmouth moccasin\', \'diamondback rattlesnake\', \'fer-de-lance\', \'garter snake\', \'gopher snake\', \'green snake\', \'hognose snake\', \'horned viper\', \'indigo snake\', \'king cobra\', \'king snake\', \'krait\', \'mamba\', \'milk snake\', \'moccasin\', \'pine snake\', \'pit viper\', \'puff adder\', \'racer\', \'rat snake\', \'rattlesnake\', \'sea serpent\', \'sea snake\', \'sidewinder\', \'taipan\', \'water moccasin\', \'water snake\', \'worm snake\', \'serpent\', \'snake\', \'viper\'], antonyms=[], stems=\'python\')\n```\n\nUsing the async interface:\n\n```python\n>>> import asyncio\n>>> asyncio.run(client.aget("python"))\nWord(word=\'python\', wordtype=\'noun\', shortdef=\'as in anaconda, boa\', synonyms=[\'adder\', \'anaconda\', \'asp\', \'black racer\', \'blacksnake\', \'blue racer\', \'boa\', \'bull snake\', \'bushmaster\', \'chicken snake\', \'cobra\', \'constrictor\', \'copperhead\', \'coral snake\', \'cottonmouth moccasin\', \'diamondback rattlesnake\', \'fer-de-lance\', \'garter snake\', \'gopher snake\', \'green snake\', \'hognose snake\', \'horned viper\', \'indigo snake\', \'king cobra\', \'king snake\', \'krait\', \'mamba\', \'milk snake\', \'moccasin\', \'pine snake\', \'pit viper\', \'puff adder\', \'racer\', \'rat snake\', \'rattlesnake\', \'sea serpent\', \'sea snake\', \'sidewinder\', \'taipan\', \'water moccasin\', \'water snake\', \'worm snake\', \'serpent\', \'snake\', \'viper\'], antonyms=[], stems=\'python\')\n```\n\nIf you want the word as a dictionary, just pass the result to `dataclasses.asdict()`:\n\n```python\n>>> from dataclasses import asdict\n>>> asdict(client.get("python"))\n{\'word\': \'python\', \'wordtype\': \'noun\', \'shortdef\': \'as in anaconda, boa\', \'synonyms\': [\'adder\', \'anaconda\', \'asp\', \'black racer\', \'blacksnake\', \'blue racer\', \'boa\', \'bull snake\', \'bushmaster\', \'chicken snake\', \'cobra\', \'constrictor\', \'copperhead\', \'coral snake\', \'cottonmouth moccasin\', \'diamondback rattlesnake\', \'fer-de-lance\', \'garter snake\', \'gopher snake\', \'green snake\', \'hognose snake\', \'horned viper\', \'indigo snake\', \'king cobra\', \'king snake\', \'krait\', \'mamba\', \'milk snake\', \'moccasin\', \'pine snake\', \'pit viper\', \'puff adder\', \'racer\', \'rat snake\', \'rattlesnake\', \'sea serpent\', \'sea snake\', \'sidewinder\', \'taipan\', \'water moccasin\', \'water snake\', \'worm snake\', \'serpent\', \'snake\', \'viper\'], \'antonyms\': [], \'stems\': \'python\'}\n```\n',
    'author': 'Peder Hovdan Andresen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PederHA/mwdictionary',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
