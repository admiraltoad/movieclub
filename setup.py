from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="movieclub",
    description="movie club tool",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="null",
    url="https://github.com/admiraltoad/movieclub",
    project_urls={
        "Issues": "https://github.com/admiraltoad/movieclub/issues",
        "CI": "https://github.com/admiraltoad/movieclub/actions",
        "Changelog": "https://github.com/admiraltoad/movieclub/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["movieclub"],
    entry_points="""
        [console_scripts]
        movieclub=movieclub.cli:cli
    """,
    install_requires=["click", "requests", "pyyaml"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
