
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

with open("version.txt") as fh:
    version = fh.read()

setuptools.setup(
    name="melan",
    version=version,
    author="Jonathan Hadida",
    author_email="jonathan.hadida@unknown.invalid",
    description="MeLan — The meta-language with Python backend.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhadida/melan",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['nxp'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
