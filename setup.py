from setuptools import setup


setup(
    name="adr-py",
    version="0.1.0",
    description="tool for managing Architecture Design Records",
    packages=["adr-py"],
    url='https://github.com/mypackage',
    author='N Ceder',
    author_email='info@naomiceder.tech',
    license='BSD-3',

    entry_points={
          'console_scripts': [
              'adr-py = adr-py.__main__:main'
          ]
       }

)


