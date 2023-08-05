import setuptools

setuptools.setup(
    name="separator-vbar",
    license="BSD New",
    version="1.1",
    author="Petr Machovec, Vaclav Barta",
    author_email="pyauth@mangrove.cz",
    description="Port of separator to Python 3",
    url="http://nlp.fi.muni.cz/projekty/rozdelovac_vet",
    packages = setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
