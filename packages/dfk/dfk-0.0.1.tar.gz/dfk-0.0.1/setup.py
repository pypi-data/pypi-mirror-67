from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="dfk",
    version="0.0.1",
    author="SysOBs",
    author_email="sob@dei.uc.pt",
    description="A command-line tool for defektor 👨‍💻",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SysOBs/dfk.git",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        dfk=dfk.cli:cli
    """,
)
