import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newrelic-api-parser", # Replace with your own username
    version="0.0.2",
    author="Bharat Sinha",
    author_email="bharat.sinha.2307@gmail.com",
    description="A plug-n-play package to start using new relic APIs for data gathering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bharat23/newrelic-api-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
      ],
    python_requires='>=3.6',
)
