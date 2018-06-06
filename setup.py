from setuptools import setup

setup(name='comet_ml_api',
    version='0.1',
    description='comet.ml API',
    url='http://github.com/storborg/funniest',
    author='Barak Ben Noon',
    author_email='bn.barak@gmail.com',
    license='MIT',
    packages=['comet_ml_api'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'])