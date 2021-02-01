from setuptools import setup, find_packages


with open("README.md", "r") as README:
    long_description = README.read()


setup(
    name="nanoAPI",
    version="0.1.0",
    author="Nandanunni A S",
    author_email="asnqln@gmail.com",
    description="A nano web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nandan-unni/Nano",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)