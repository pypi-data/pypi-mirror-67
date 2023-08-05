from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='hestia_earth.validation',
    packages=find_packages(),
    version='0.0.0',
    description='Hestia Data Validation library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Guillaume Royer',
    author_email='guillaumeroyer.mail@gmail.com',
    license='GPL-3.0-or-later',
    url='https://gitlab.com/hestia-earth/hestia-data-validation',
    keywords=['hestia', 'data', 'validation'],
    classifiers=[],
    install_requires=[],
    python_requires='>=3'
)
