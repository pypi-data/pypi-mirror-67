from setuptools import setup

setup(
  name='cockroach-poker',
  version='0.1.3',
  description='A fun card game all about bluffing',
  url='https://gitlab.com/oldironhorse/cockroach-poker',
  author='Simon Redding',
  author_email='s1m0n.r3dd1ng@gmail.com',
  packages=['cockroachpoker'],
  install_requires=[
        'pycryptodome',
        'paho-mqtt',
        'click'
      ],
  scripts=[
      'bin/cockroach-host',
      'bin/cockroach-player'],
  python_requires='>=3.5',
  test_suite='nose.collector',
  tests_require=['nose'],
  zip_safe=False)
