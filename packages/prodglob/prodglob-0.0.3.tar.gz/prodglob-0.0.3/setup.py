import setuptools

USERNAME = 'beasteers'
NAME = 'prodglob'

setuptools.setup(
    name=NAME,
    version='0.0.3',
    description='Lightweight glob extensions with extended path joining.',
    long_description=open('README.md').read().strip(),
    long_description_content_type='text/markdown',
    author='Bea Steers',
    author_email='bea.steers@gmail.com',
    url='https://github.com/{}/{}'.format(USERNAME, NAME),
    packages=setuptools.find_packages(),
    # entry_points={'console_scripts': ['{name}={name}:main'.format(name=NAME)]},
    install_requires=[],
    license='MIT License',
    keywords='glob product os.path.join join file sort make'
)
