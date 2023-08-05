import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simcomponentsdorachua", # Replace with your own username
    version="0.0.5",
    author="Dora Chua",
    author_email="msdorachua@gmail.com",
    description="A small package for simulating RaspberryPi and Arduino hardware components on a Windows PC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)