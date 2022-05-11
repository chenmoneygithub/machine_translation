from setuptools import find_packages
from setuptools import setup

setup(
    name="trainer",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="Machine translation training (transformer).",
    install_requires=[
        "absl-py",
        "numpy",
        "packaging",
        "tensorflow",
        "tensorflow_text",
        "datasets",
        "keras-nlp",
    ],
)
