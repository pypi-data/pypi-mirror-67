import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sarscov2summary",
    version="0.5",
    author="Sergei Pond",
    author_email="spond@temple.edu",
    description="Summarizes outputs of Galaxy SARS-CoV2 Selection Analysis workflow",
    install_requires=['biopython'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickeener/sarscov2summary",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['sarscov2summary=sarscov2summary.cli:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: Academic Free License (AFL)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

