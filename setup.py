from setuptools import setup
import os

import stopspam

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

install_requires = [
]

setup(name='stopspam',
      version=stopspam.__version__,
      description="Detect spam. Stop Spam. Simple",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Development Status :: 3 - Alpha",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Natural Language :: English",
          "Topic :: Internet :: WWW/HTTP :: Site Management",
          "Topic :: Utilities",
      ],
      keywords='spam',
      author='Paul Hallett',
      author_email='hello@phalt.co',
      url='http://github.com/phalt/stopspam',
      license='GPL3',
      packages=['stopspam'],
      package_dir={'stopspam': 'stopspam'},
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
          'console_scripts': ['stopspam=stopspam:main']
      })
