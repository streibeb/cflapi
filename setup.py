import setuptools
import sys, os

with open("README.md", "r") as fh:
    long_description = fh.read()

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

setuptools.setup(
    name="cflapi",
    version="1.0.2",
    author="Brayden Streibel",
    author_email="brayden@streibel.ca",
    description="Canadian Football League API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/streibeb/cflapi",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['requests'],
    license='MIT',
)