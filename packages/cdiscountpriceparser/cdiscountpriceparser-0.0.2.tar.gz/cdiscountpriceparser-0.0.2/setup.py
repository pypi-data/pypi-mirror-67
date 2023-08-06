from setuptools import setup
setup(
    name='cdiscountpriceparser',
    version='0.0.2',
    description='price parser of cdiscount product.',
    package_dir={'cdiscount_parser': 'cdiscount_parser'},
    packages=["cdiscount_parser"],
    install_requires=[
        "beautifulsoup4 ~= 4.9.0",
        "urllib3 ~= 1.25.9",
        "regex ~= 2020.4.4"
    ],
    extras_require={
        "dev": [
            "pytest>=5.4.1"
        ]
    },
    url="https://github.com/pierredarrieutort/cdiscrap",
    author="mathieudaix, pierredarrieutort",
    author_email="mathieudaixpro@gmail.com, p.darrieutort@outlook.fr"
)
