import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stormheron-mead-calc",
    version="0.2",
    author="Stormheron",
    description="an abstraction layer for the stormheron mead-calc API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/stormheron/mead-calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["mead"],
)
