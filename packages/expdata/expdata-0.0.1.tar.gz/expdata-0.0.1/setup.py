import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="expdata",  # Replace with your own username
    version="0.0.1",
    author="Ömer Faruk Sarı",
    author_email="f.omer.sari@outlook.com",
    description="A package that helps data exploration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omerfaruksari/expdata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)