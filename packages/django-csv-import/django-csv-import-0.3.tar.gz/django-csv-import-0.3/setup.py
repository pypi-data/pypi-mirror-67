import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-csv-import",
    version="0.3",
    author="Abhinav Dev",
    author_email="theabhinavdev@gmail.com",
    description="Library to upload csv directly through django admin interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DevAbhinav2073/csv_importer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'django',
    ],
    python_requires='>=3.6',
    include_package_data=True
)
