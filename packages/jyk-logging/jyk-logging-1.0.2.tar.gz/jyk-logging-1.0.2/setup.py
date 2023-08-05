import codecs
import os
import re

from setuptools import setup, find_packages


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)

    return codecs.open(path, mode, encoding)


with open_local(["src/python/jyk/logging", "__init__.py"],
                encoding="latin1") as fp:
    try:
        version = re.findall(r"^__version__ = \"([^']+)\"\r?$", fp.read(),
                             re.M)[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")

with open('README.md') as f:
    long_description = f.read()

setup(name="jyk-logging",
      version=version,
      url="https://git.kongkongss.com/jyker/jyk-logging",
      author="Kongkong Jiang",
      author_email="jyk.kongkong@gmail.com",
      description="jyk logging utils package",
      keywords="jyk logging",
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="MIT",
      python_requires=">=3.7.1",
      packages=find_packages('src/python'),
      package_dir={'': 'src/python'},
      include_package_data=True,
      namespace_packages=['jyk'])
