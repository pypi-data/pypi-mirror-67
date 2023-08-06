from distutils.core import setup

setup(
    name='KiaUvo',
    packages=['KiaUvo'],
    version='0.8',
    license='MIT',
    description='API Wrapper for the Kia Uvo service',
    author='William Comartin',
    author_email='williamcomartin@gmail.com',
    url='https://github.com/wcomartin/kiauvo',
    download_url='https://github.com/wcomartin/kiauvo/archive/v_05.tar.gz',
    keywords=['Kia', 'Uvo', 'Api'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
