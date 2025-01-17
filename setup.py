from setuptools import setup, find_packages

setup(
    name="pass_phrase_generator",
    version="0.1.0",
    author="Joel Kramer",
    author_email="joelkramer@gmail.com",
    description="Generate a pass phrase from a set of common words",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Grippr/pass-phrase-generator",
    packages=find_packages(where="src"),
    package_dir={"": "src"}, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    entry_points = {
        'console_scripts': ['pass-phrase-generator=pass_phrase_generator.pass_phrase_generator:main'],
    }
)