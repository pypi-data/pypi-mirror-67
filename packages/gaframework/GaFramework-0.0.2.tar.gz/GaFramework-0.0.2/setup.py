import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GaFramework", # Replace with your own username
    version="0.0.2",
    author="John Newcombe",
    author_email="jnewcombeuk@gmail.com",
    description="Simple to use genetic algorithm library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/johnnewcombe/gapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ],
    python_requires='>=3.6',
)
