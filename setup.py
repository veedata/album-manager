import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()

setuptools.setup(
    name='memories',
    version='1.0.0',
    url='https://github.com/veedata/memories',
    download_url='https://github.com/veedata/memories/archive/refs/tags/v1.0.0-stable.tar.gz',
    author='Viraj Thakkar',
    author_email='vdthakkar111@gmail.com',
    description='A library for those who want to convert their older images into digitised format (with metadata), and beautify them using borders and other options.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    keywords=['computer vision', 'image processing', 'opencv', 'album'],
    project_urls={
        "Code": "https://github.com/veedata/memories",
        "Issue tracker": "https://github.com/veedata/memories/issues",
        'Documentation': "https://memories.readthedocs.io/en/latest",
    },
    install_requires=[
        'requests',
        'piexif',
        'opencv-python',
        'Pillow',
    ],
    extras_require={
        'test': [
            'imagehash',
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_dir={"": "memories"},
    packages=setuptools.find_packages(where="memories"),
    test_suite='tests',
)
