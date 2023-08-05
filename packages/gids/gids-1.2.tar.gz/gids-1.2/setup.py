import setuptools

setuptools.setup(
    name='gids',
    version='1.2',
    license='',
    author_email="gkswlsrb95@gmail.com",
    description="Google-images-downloader module using selenium",
    install_requires=[
        'beautifulsoup4==4.9.0',
        'certifi==2020.4.5.1',
        'chardet==3.0.4',
        'idna==2.9',
        'requests==2.23.0',
        'selenium==3.141.0',
        'soupsieve==2.0',
        'urllib3==1.25.9'
    ],
    python_requires = '>=3',
    long_description=open('README.md').read(), 
    url="https://github.com/jinkyuhan/google-images-download",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)