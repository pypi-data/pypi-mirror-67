import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="owlet",
    version="0.0.1",
    author="HFM3",
    # author_email="author@example.com",
    description="A Geospatial Python Package for Field Researchers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/HFM3/owlet',
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
    ],
    python_requires='>=3.8',
)

# https://github.com/pypa/sampleproject/blob/master/setup.py
