from setuptools import setup, find_packages

setup(
    name='helloworld Jayaraj',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    tests_require=[
        'pytest',
    ],
)
