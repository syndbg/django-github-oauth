from setuptools import setup, find_packages
import os
import os.path


def _get_version(here):
    with open(os.path.join(here, "github_oauth", "__init__.py")) as f:
        for line in f.readlines():
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip('"')

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)
VERSION = _get_version(ROOT_DIR)

setup(
    name="django-github-oauth",
    version=VERSION,
    description="Django Github OAuth package.",
    author="Anton Antonov",
    author_email="anton.synd.antonov@gmail.com",
    url="https://github.com/syndbg/django-github-oauth",
    license='MIT License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Utilities'],
    install_requires=[
        'requests>=2.3.0'
    ],
)
