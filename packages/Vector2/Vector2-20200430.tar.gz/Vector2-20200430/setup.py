import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Vector2",
    version="20200430",
    author="philip r brenan",
    author_email="philiprbrenan@gmail.com",
    description="Vectors in 2 dimensional Euclidean space",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/Vector2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
