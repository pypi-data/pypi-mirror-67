from setuptools import setup

with open("README.md", "r") as fh:
    long_description= fh.read()


setup(
    name='mathieu-pierre-cdiscrap',
    version='0.0.1',
    description='Python package capable of raising the price of any product on the site www.cdiscount.com',
    py_modules=["sku_to_price", "sku", "price"],
    package_dir={'': 'price_parser'},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'beautifulsoup4',
        'urllib.request',
        're'
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7"
        ]
    },
    url="https://github.com/pierredarrieutort/cdiscrap",
    author="Mathieu Daix, Pierre Darrieutort",
    author_email="mathieudaixpro@gmail.com, p.darrieutort@outlook.fr"
)
