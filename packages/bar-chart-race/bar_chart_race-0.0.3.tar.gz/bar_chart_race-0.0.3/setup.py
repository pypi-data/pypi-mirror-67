import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

pat = r'!\[gif\]\('
repl = r'![gif](https://raw.githubusercontent.com/dexplo/bar_chart_race/master/'
long_description = re.sub(pat, repl, long_description)

setuptools.setup(
    name="bar_chart_race",
    version="0.0.3",
    author="Ted Petrou",
    author_email="petrou.theodore@gmail.com",
    description="Creates animated bar chart races using matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dexplo/bar_chart_race",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)