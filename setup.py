from setuptools import setup, find_packages

setup(
    name='better-json',
    version='0.1.0',
    description='A streamlined JSON read/write handler',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pbower',
    author_email='N/A',
    url='https://github.com/pbower/better-json',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
