from setuptools import setup, find_packages

setup(
    name="Advent of Code",
    version="0.1.0",
    author="Brian Lindawson",
    author_email="brianlindawson@gmail.com",
    install_requires=[
        "numpy",
        "pandas",
        "pathlib",
    ],
    extras_require={"dev": ["pytest", "black", "pylint", "flake8", "ipykernel"]},
    python_requires=">=3.8",
)
