from setuptools import setup, find_packages

setup(
    name="examtool",
    version="0.1.2",
    author="Rahul Arya",
    author_email="rahularya@berkeley.edu",
    licence="MIT",
    packages=find_packages(include=["apps"]),
    entry_points={
        "console_scripts": [
            "examtool=cli.__main__:cli",
        ]
    }, install_requires=['click', 'pikepdf', 'pytz', 'requests', 'fpdf', 'cryptography']
)
