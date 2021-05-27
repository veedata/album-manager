from distutils.core import setup

setup(
    name = 'memories',
    packages = ['memories'],
    version = '0.2',
    description = 'A library for those who want to convert their older images into digitised format (with metadata), and beautify them using borders and other options.',
    author = 'Viraj Thakkar',
    author_email = 'vdthakkar111@gmail.com',
    url = 'https://github.com/veedata/album-manager',
    download_url = 'https://github.com/veedata/album-manager/archive/refs/tags/v0.1-alpha.tar.gz',
    keywords = ['computer vision', 'image processing', 'opencv'],
    install_requires=[
          'piexif',
      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
    ],
    scripts=['bin/range-detector'],
)