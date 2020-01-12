# copied from https://github.com/pypa/sampleproject/blob/master/setup.py

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='grammar',
    version='0',
    description='Pythonic grammar creation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bfoz/grammar-python',
    author='Brandon Fosdick',
    author_email='bfoz@bfoz.net',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    keywords='recursive descent parser parse parsing grammar',
    package_dir={'':'grammar'},
    py_modules=['grammar'],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/bfoz/grammar-python/issues',
        'Source': 'https://github.com/bfoz/grammar-python/',
    },
)
