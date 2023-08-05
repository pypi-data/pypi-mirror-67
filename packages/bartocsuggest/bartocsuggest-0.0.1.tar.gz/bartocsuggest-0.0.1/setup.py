import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bartocsuggest", # Replace with your own username
    version="0.0.1",
    author="Maximilian Hindermann",
    author_email="maximilian.hindermann@unibas.ch",
    description="A vocabulary suggestion tool using the BARTOC FAST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MHindermann/bartocsuggest",
    packages=setuptools.find_packages(),
    install_requires=[
        "urllib3",
        "requests",
        "python-Levenshtein-wheels",
        "openpyxl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)