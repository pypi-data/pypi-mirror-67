from setuptools import setup

setup(name='adn_tools',
      version='0.1',
      description='A helper that converts XLSX to api calls.',
      url='http://github.com/test/test',
      author='Mikael Lundin',
      author_email='mikael@adnuntius.com',
      license='MIT',
      packages=['adn_tools'],
      install_requires=[
          'requests',
          'pandas',
          'xlrd'
      ],
      zip_safe=False)
