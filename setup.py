
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
  long_description = readme.read()

setup(
  name="psdtoolkit-util",
  version="0.1.0",
  description="Home maid parameter encoder and decoder for PSDToolKit 0.1.3.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="tikubonn",
  author_email="https://twitter.com/tikubonn",
  url="https://github.com/tikubonn/psdtoolkit-util",
  license="MIT",
  packages=find_packages(),
  install_requires=[],
  dependency_links=[],
  entry_points={},
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License",
  ],
  test_suite="test"
)
