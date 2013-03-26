from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'readme.txt')).read()
NEWS = open(os.path.join(here, 'news.txt')).read()

install_requires = [
]


setup(name='stopspam',
      version='0.2.2',
      description="Detect spam. Stop Spam. Simple",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
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
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['stopspam=stopspam:main']
    }
)