from setuptools import setup, find_packages

requires = [
    'requests',
    'SQLAlchemy',
    'beautifulsoup4',
    'lxml',
    'xmltodict',
]

DESCRIPTION = 'News feed by telegram bot'
LONG_DESCRIPTION = 'Python program package for automatically fetching news and pushing by telegram bot'

setup(
    name='telegram-news-eswzy',     # TODO: Temp name!
    version='0.0.5',
    author='ESWZY',
    author_email='0903wzy@gmail.com',
    url='https://github.com/ESWZY/telegram-news',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    python_requires='>=3.5',
    install_requires=requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Office/Business :: News/Diary",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
