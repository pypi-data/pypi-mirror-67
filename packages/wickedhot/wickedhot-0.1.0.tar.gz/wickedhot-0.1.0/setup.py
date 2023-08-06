# following this
# https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='wickedhot',
    version='0.1.0',
    description='Wicked easy one-hot-encoding in pure python with no dependencies',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='David Johnston',
    author_email='dave31415@gmail.com',
    keywords=['one-hot encoding', 'machine learning'],
    url='https://github.com/dave31415/wickedhot',
    download_url='https://pypi.org/project/wickedhot/'
)

install_requires = [
    'pytest'
]

if __name__ == '__main__':
    setup(include_package_data=True, install_requires=install_requires, **setup_args)

