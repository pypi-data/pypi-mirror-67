import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atlassian-cloud",  # Replace with your own username
    version="0.0.1",
    author="Régis Tremblay Lefrancois",
    author_email="rtlefrancois@agri-marche.com",
    description="Python module for Atlassian Cloud REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests>=2.23.0"],
)
