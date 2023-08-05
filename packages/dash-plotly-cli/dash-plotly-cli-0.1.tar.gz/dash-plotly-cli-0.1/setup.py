from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(this_directory, 'entrypoint.txt'), encoding='utf-8') as f:
    entry_points = f.read()

setup(
    name='dash-plotly-cli',
    version='0.1',
    py_modules=['dash-plotly-cli'],
    keywords=['dash', 'plotly', 'cli', ],
    packages=find_packages(),
    install_requires=[
        'Click',
        'Cookiecutter',
    ],
    python_requires='>=3.5',
    include_package_data=True,
    entry_points=entry_points,
    author='Christopher J. Adkins',
    author_email='chris@cjadkins.com',
    license='MIT',
    description='A cli for creating and working on dash apps',
    url='https://github.com/Softyy/dash-cli',
    download_url='https://github.com/Softyy/dash-cli/tags',
    platforms='any',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
