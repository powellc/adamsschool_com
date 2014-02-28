from setuptools import setup, find_packages
import os

#version = __import__('.__init__.py').__version__
version = "2.0"

install_requires = [
    'setuptools',
    'django',
    'django-cms',
]

setup(
    name = "adamsschool_com",
    version = version,
    url = 'http://bitbucket.org/powellc/adamsschool_com',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "The adamsschool.com web site.",
    author = "Colin Powell",
    author_email = 'colin.powell@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'adamsschool_com': 'adamsschool_com',
    },
)