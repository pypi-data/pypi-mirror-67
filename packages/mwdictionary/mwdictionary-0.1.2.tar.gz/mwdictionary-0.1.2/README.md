# mwdictionary

Small wrapper around the Merriam-Webster API. Has both a sync and async interface thanks to [httpx](https://github.com/encode/httpx).

## Installation

`pip install mwdictionary`

## Usage

Using mwdictionary's sync interface:

```python
>>> from mwdictionary import MWClient
>>> client = MWClient(key="YOUR-KEY-HERE")
>>> client.get("python")
Word(word='python', wordtype='noun', shortdef='as in anaconda, boa', synonyms=['adder', 'anaconda', 'asp', 'black racer', 'blacksnake', 'blue racer', 'boa', 'bull snake', 'bushmaster', 'chicken snake', 'cobra', 'constrictor', 'copperhead', 'coral snake', 'cottonmouth moccasin', 'diamondback rattlesnake', 'fer-de-lance', 'garter snake', 'gopher snake', 'green snake', 'hognose snake', 'horned viper', 'indigo snake', 'king cobra', 'king snake', 'krait', 'mamba', 'milk snake', 'moccasin', 'pine snake', 'pit viper', 'puff adder', 'racer', 'rat snake', 'rattlesnake', 'sea serpent', 'sea snake', 'sidewinder', 'taipan', 'water moccasin', 'water snake', 'worm snake', 'serpent', 'snake', 'viper'], antonyms=[], stems='python')
```

Using the async interface:

```python
>>> import asyncio
>>> asyncio.run(client.aget("python"))
Word(word='python', wordtype='noun', shortdef='as in anaconda, boa', synonyms=['adder', 'anaconda', 'asp', 'black racer', 'blacksnake', 'blue racer', 'boa', 'bull snake', 'bushmaster', 'chicken snake', 'cobra', 'constrictor', 'copperhead', 'coral snake', 'cottonmouth moccasin', 'diamondback rattlesnake', 'fer-de-lance', 'garter snake', 'gopher snake', 'green snake', 'hognose snake', 'horned viper', 'indigo snake', 'king cobra', 'king snake', 'krait', 'mamba', 'milk snake', 'moccasin', 'pine snake', 'pit viper', 'puff adder', 'racer', 'rat snake', 'rattlesnake', 'sea serpent', 'sea snake', 'sidewinder', 'taipan', 'water moccasin', 'water snake', 'worm snake', 'serpent', 'snake', 'viper'], antonyms=[], stems='python')
```

If you want the word as a dictionary, just pass the result to `dataclasses.asdict()`:

```python
>>> from dataclasses import asdict
>>> asdict(client.get("python"))
{'word': 'python', 'wordtype': 'noun', 'shortdef': 'as in anaconda, boa', 'synonyms': ['adder', 'anaconda', 'asp', 'black racer', 'blacksnake', 'blue racer', 'boa', 'bull snake', 'bushmaster', 'chicken snake', 'cobra', 'constrictor', 'copperhead', 'coral snake', 'cottonmouth moccasin', 'diamondback rattlesnake', 'fer-de-lance', 'garter snake', 'gopher snake', 'green snake', 'hognose snake', 'horned viper', 'indigo snake', 'king cobra', 'king snake', 'krait', 'mamba', 'milk snake', 'moccasin', 'pine snake', 'pit viper', 'puff adder', 'racer', 'rat snake', 'rattlesnake', 'sea serpent', 'sea snake', 'sidewinder', 'taipan', 'water moccasin', 'water snake', 'worm snake', 'serpent', 'snake', 'viper'], 'antonyms': [], 'stems': 'python'}
```
