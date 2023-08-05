import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="letterpress", # Replace with your own username
    version="0.0.1",
    author="LittleCoder",
    author_email="i7meavnktqegm1b@qq.com",
    description="batch docx generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/littercodersh/letterpress",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['python-docx', 'xlwings'],
    python_requires='>=3',
)
