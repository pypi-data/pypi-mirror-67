import os
from setuptools import (
    find_packages,
    setup,
)


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='django_simple_bulk_emailer',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app for sending bulk email',
    long_description=README,
    url='http://www.jonathanrickard.com/',
    author='Jonathan Rickard',
    author_email='jonathan.rickard@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=2.2.9,<3.0',
        'django-admin-sortable2>=0.6.21',
        'django-ckeditor>=5.6.1',
        'django-simple-file-handler>=0.2.4',
        'mailchimp3>=3.0',
        'Pillow>=5.0',
        'requests>=2.21.0',
    ],
)
