import setuptools

print(setuptools.find_packages())

setuptools.setup(
    name="cloudwright_trello",
    version="0.0.0",
    author="cloudwright",
    url="https://cloudwright.io",
    author_email="founders@cloudwright.io",
    description="cloudwright_trello",
    packages=setuptools.find_packages(),
    install_requires=[ ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)
