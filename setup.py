from setuptools import find_packages, setup

# Main dependencies
install_requires = [
    "snowflake-connector-python>=3.0.0",
    "pyspark>=3.3.0"  # Always pin minimum versions
]

# Testing tools (optional)
tests_require = [  # Changed from test_requires to standard name
    "pytest>=7.0",
    "pytest-mock>=3.0"
]

# Development tools (optional)
extras_require = {  # Proper way to handle optional dependencies
    "dev": [
        "pre-commit>=2.0",
        "dbx>=0.8", 
        "pyright>=1.0"
    ] + tests_require,
    "test": tests_require  # Separate test group
}

setup(
    name="default_package",
    version="0.0.0",
    packages=find_packages(),  # You forgot this!
    install_requires=install_requires,
    tests_require=tests_require,  # For `python setup.py test`
    extras_require=extras_require,  # For `pip install .[dev]`
    python_requires=">=3.8"  # Always specify Python version
)
