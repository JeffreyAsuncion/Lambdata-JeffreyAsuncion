import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_jeffreyasuncion",  # Replace with your own username
    version="0.0.14",
    author="Jeffrey Asuncion",
    author_email="jeffrey.l.asuncion@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffreyAsuncion/Lambdata-JeffreyAsuncion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
