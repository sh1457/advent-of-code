import setuptools

setuptools.setup(
    name='aocsolver',
    version='0.1.0',
    description='Solver helper of Advent of code',
    long_description='Solver helper of Advent of code',
    long_description_content_type='text/markdown',
    author='Sujith Sudarshan',
    author_email='sh1457@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/sh1457/advent-of-code',
    py_modules=['solver'],
    entry_points={
        'console_scripts': ["solve=solver:solve"],
    },
    install_requires=['click'],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
