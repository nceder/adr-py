from setuptools import setup


setup(
    name="adrpy",
    version="0.1.0",
    description="tool for managing Architecture Design Records",
    packages=["adrpy"],
    url='https://github.com/mypackage',
    author='N Ceder',
    author_email='info@naomiceder.tech',
    license='BSD-3',

    entry_points={
          'console_scripts': [
              'adrpy=adrpy.__main__:main'
          ]
       }

)


