from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


setup(
	name='dexonlineBK',
	version='0.1.0',
	description='Dexonline.ro API for Python',
	author='Alexandru Petrachi (BlackKakapo)',
	packages=['dexonlineBK'],
	zip_safe=False,
	url='https://github.com/BlackKakapo/dexonline-API',
	long_description=long_description,
    long_description_content_type='text/markdown',
	install_requires=['requests', 'bs4', 'html5lib', 'random']
)