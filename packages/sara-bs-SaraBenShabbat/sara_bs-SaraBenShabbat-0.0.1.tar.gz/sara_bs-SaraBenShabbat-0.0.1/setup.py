import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sara_bs-SaraBenShabbat", # Replace with your own username
    version="0.0.1",
    author="Sara Ben Shabbat",
    author_email="sarabenshabbat@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["sara_bs"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)