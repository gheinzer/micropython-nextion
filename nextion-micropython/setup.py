import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython-nextion", # Replace with your own username
    version="1.0",
    author="Gabriel Heinzer",
    author_email="dev@gabrielheinzer.ch",
    description="Nextion Library for Micropython.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/programmer372/micropython-nextion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Micropython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["nextion-micropython"],
    include_package_data=True,
    entry_points=
)