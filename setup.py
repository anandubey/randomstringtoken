import pathlib
from setuptools import setup

# The directory containing this file
CURR_DIR = pathlib.Path(__file__).parent

# The text of the README file
README = (CURR_DIR / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="randomstringtoken",
    version="0.2",
    description="Generate random string token of specified length",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/p5ypher/randomstringtoken",
    author="Anand Kumar Dubey",
    author_email="dubey.anandkr@gmail.com",
    license="BSD 3-Clause License",
    classifiers=[
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
    ],
    packages=["randomstringtoken"],
    include_package_data=False,
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "randomstringtoken=randomstringtoken.__main__:main",
        ]
    },
)