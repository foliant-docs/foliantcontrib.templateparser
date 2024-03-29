from setuptools import setup, find_namespace_packages


SHORT_DESCRIPTION = 'Template parser preprocessor for Foliant.'

try:
    with open('README.md', encoding='utf8') as readme:
        LONG_DESCRIPTION = readme.read()

except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


setup(
    name='foliantcontrib.templateparser',
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    version='1.0.6',
    author='Daniil Minukhin',
    author_email='ddddsa@gmail.com',
    url='https://github.com/foliant-docs/foliantcontrib.templateparser',
    packages=find_namespace_packages(),
    license='MIT',
    platforms='any',
    install_requires=[
        'foliant>=1.0.8',
        'foliantcontrib.utils>=1.0.2',
        'foliantcontrib.meta>=1.2.0',
        'jinja2'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ]
)
