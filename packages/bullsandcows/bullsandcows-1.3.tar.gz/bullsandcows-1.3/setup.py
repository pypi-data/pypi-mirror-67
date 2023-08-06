from setuptools import setup

with open("README.md","r")as f:
    long_description = f.read()
setup(
    name = "bullsandcows",
    version = "1.3",
    description = "Bulls and Cows in Python.",
    py_modules = ["bullsandcows"],
    package_dir = {"":"src"},
    author = "ryancflam",
    author_email = "ryancflam@hotmail.com",
    url = "https://github.com/ryancflam/Bulls-and-Cows",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)