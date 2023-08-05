import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maliarov",
    version="0.1.15",
    description="Routine automation",

    packages=['maliarov'],
    include_package_data = True,
    package_data = {
        '': ['*.txt'],
        'maliarov': ['data/*.*'],
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "selenium ~= 3.1",
        "datetime ~= 4.3",
        "beautifulsoup4 ~= 4.8.2",
        "urllib3 ~= 1.25.8"
    ],
    author="Anatolii Maliarov",
    author_email="tly.mov@gmail.com",
    url="https://github.com/tlmy/webscraping",
)
