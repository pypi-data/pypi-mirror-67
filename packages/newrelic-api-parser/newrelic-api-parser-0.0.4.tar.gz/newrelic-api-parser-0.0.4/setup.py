import setuptools

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="newrelic-api-parser",
    package=['newrelic-api-parser'],
    version="0.0.4",
    author="Bharat Sinha",
    author_email="bharat.sinha.2307@gmail.com",
    description="A plug-n-play package to start using new relic APIs for data gathering",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Bharat23/newrelic-api-parser",
    packages=setuptools.find_packages(),
    license='MIT',
    keywords = ['new relic api', 'insights', 'new relic'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    install_requires=[
          'requests',
      ],
    python_requires='>=3.6',
)
