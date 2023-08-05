from setuptools import setup, find_packages

requires = [
    'requests',
    'SQLAlchemy',
    'beautifulsoup4',
    'lxml',
    'xmltodict',
]

DESCRIPTION = 'News feed by telegram bot'
LONG_DESCRIPTION = 'Python program structure for automatically fetch news and push by telegram bot.'

setup(
    name='telegram-news-eswzy',     # Temp name
    version='0.0.3',
    author='ESWZY',
    author_email='',
    url='https://github.com/ESWZY/telegram-news',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['telegram_news'],
    include_package_data=True,
    license="MIT",
    python_requires='>=3.5',
    install_requires=requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
