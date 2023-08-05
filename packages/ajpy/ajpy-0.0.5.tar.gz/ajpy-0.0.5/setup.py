from setuptools import setup

setup(
    name = "ajpy",
    packages = ["ajpy"],
    version = "0.0.5",
    description = "AJP package crafting library",
    author = "Julien Legras",
    author_email = "julien.legras@synacktiv.com",
    url = "https://github.com/hypn0s/AJPy/",
    download_url = "https://github.com/hypn0s/AJPy/archive/master.zip",
    license = "BSD",
    keywords = ["ajp", "java", "network"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Topic :: System :: Networking",
        ],
    long_description = """\
AJPy aims to craft AJP requests in order to communicate with AJP connectors.
"""
)
