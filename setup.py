import setuptools

setuptools.setup(
    name="SolveLed",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Conor Hopkins",
    author_email="conor.hopkins@ucdconnect.ie",

    description="led assignment for comp30670",
    long_description=open('docs/README.md').read(),
    package=['SolveLed'],
#    packages=setuptools.find_packages(),

    install_requires=[
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points = {
        'console_scripts': ['solveled=SolveLed.main:main'],
    }
)
