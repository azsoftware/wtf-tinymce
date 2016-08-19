import os
import re
from io import open
from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version file
with open(os.path.join(root, 'wtf_tinymce', '_version.py'), encoding='utf-8') as f:
    version_file = f.read()

mo = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", version_file, re.M)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError('Unable to find version string in wtf_tinymce/_version.py.')

requires = [
    'bleach',
    'WTForms>=2.0',
    'Flask>=0.10.0',
    'Flask-WTF',
    ]


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wtf-tinymce',
    version=version,
    description='TinyMCE editor extension for WTForms',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        ],
    author='Alexander Zhygailo',
    author_email='alexander777vz@gmail.com',
    url='https://github.com/azsoftware/wtf-tinymce',
    keywords='wtf-tinymce, wtforms, tinymce, richeditor',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    install_requires=requires,
    tests_require=[],
    dependency_links=[]
)
