import setuptools
import os


readme_dir = os.path.dirname(__file__)
readme_path = os.path.join(readme_dir, 'README.md')
with open(readme_path, "r") as f:
    long_description = f.read()


required_packages = [
    "sklearn",
    "numpy",
    "pandas",
    "python-dateutil",
    "proteinko==4.0",
]


setuptools.setup(
    name="mhclovac",
    version="2.1",
    author="Stefan Stojanovic",
    author_email="stefs304@gmail.com",
    description="MHC binding prediction based on modeled "
                "physicochemical properties of peptides",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefs304/mhclovac",
    packages=[
        'mhclovac',
    ],
    package_data={
        'mhclovac': ['trained_models'],
    },
    install_requires=required_packages,
    entry_points={
          'console_scripts': [
              "mhclovac=mhclovac.mhclovac_run:main",
          ]
    },
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry"
    )
)
