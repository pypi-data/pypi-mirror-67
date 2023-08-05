import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streetcred-id-service-clients",
    version="0.1.1",
    author="Streetcred ID",
    author_email="michael.black@streetcred.id",
    description="Service Clients for our Agency and Custodian API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streetcred-id/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
