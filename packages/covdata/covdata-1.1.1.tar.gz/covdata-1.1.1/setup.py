import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covdata",
    version="1.1.1",
    author="Dripta senapati",
    author_email="driptasenapati97@gmail.com",
    description="A package that can grab all data of Covid-19 cases in India",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kalyaniuniversity/covidindia",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.1',
        'matplotlib>=3.1.3',
        'datetime'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "covdata=covdata.cli:main",
        ]
    },
    python_requires='>=3.6',
)
