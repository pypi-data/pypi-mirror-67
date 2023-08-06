from setuptools import setup
from pathlib import Path

long_description: str = Path(Path.cwd(), "README.md").read_text()


setup(
    name="AutoMD",
    version="1.0.0",
    url="https://github.com/cliftbar/automd",
    license="MIT",
    author="Cameron Barclift",
    author_email="cwbarclift@gmail.com",
    description="AutoMD is a documentation library for Flask APIs build with FlaskRESTful and Webargs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'automd': 'automd'},
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "flask",
        "flask-restful",
        "flask-cors",
        "webargs",
        "apispec"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
