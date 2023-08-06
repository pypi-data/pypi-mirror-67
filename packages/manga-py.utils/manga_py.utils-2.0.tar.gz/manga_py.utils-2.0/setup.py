from setuptools import find_packages, setup


version = '2.0'
author = 'Sergey Zharkov'


REQUIREMENTS = ['lxml', 'cssselect', 'pycryptodome', 'cloudscraper', 'requests~=2.20', 'packaging', 'js2py', 'tinycss2', ]


release_status = '5 - Production/Stable'
if ~version.find('beta'):
    release_status = '4 - Beta'
if ~version.find('alpha'):
    release_status = '3 - Alpha'


setup(
    name='manga_py.utils',
    version=version,
    license='MIT',
    author=author,
    packages=find_packages(exclude=('tests', '.mypy_cache')),
    keywords="Manga, crawler, Manga crawler providers",
    zip_safe=True,
    include_package_data=True,
    namespace_packages=['manga_py', ],
    classifiers=[
        'Development Status :: %s' % (release_status,),
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
    install_requires=REQUIREMENTS,
    python_requires='>=3.6'
)