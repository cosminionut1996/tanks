import setuptools

with open("readme", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tank", # Replace with your own username
    version="0.0.1",
    author="Cosmin Ionut",
    author_email="cosminionut1996@yahoo.com",
    description="Tank object component common across multiple app modules.",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
