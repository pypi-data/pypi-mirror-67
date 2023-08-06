import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlod",
    version="2.0.1",
    author="WWW.JLOD.ORG",
    author_email="contact@jload.org",
    description="Local Document Oriented Database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.jlod.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
