from setuptools import setup

setup(
    packages=['imgvalidator'],
    test_suite="tests",
    install_requires=['py3exiv2bind'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
         "console_scripts": [
             'imgvalidator = imgvalidator.__main__:main'
         ]
     },
    zip_safe=False,
)
