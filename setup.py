from setuptools import setup, find_packages

setup(
    name="mdplistlib",
    version="0.1.1",
    description="A library for parsing DEBA/MDPLIST files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="John Hyla",
    author_email="jfhyla@gmail.com",
    url="https://github.com/snoop168/mdplistlib",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mdplist-cli=mdplist.mdplist_cli:main",
        ],
    },
    python_requires=">=3.6",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)