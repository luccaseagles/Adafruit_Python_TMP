from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'Adafruit_TMP',
      version           = '1.0.0',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Library for accessing the TMP006 non-contact temperature sensor on a Raspberry Pi or Beaglebone Black.',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_TMP/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.5.0'],
      install_requires  = ['Adafruit-GPIO>=0.5.0'],
      packages          = find_packages())