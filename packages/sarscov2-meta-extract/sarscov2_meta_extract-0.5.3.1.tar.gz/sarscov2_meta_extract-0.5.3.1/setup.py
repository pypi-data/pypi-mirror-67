import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sarscov2_meta_extract",
    version="0.5.3.1",
    author="Nick Keener",
    author_email="nickeener@gmail.com",
    description="Extracts metadata from MSA for Galaxy workflow",
    install_requires=['biopython'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickeener/sarscov2_meta_extract",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['sarscov2_meta_extract=sarscov2metaextract.cli:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Academic Free License (AFL)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

