from setuptools import setup
# NOT 
setup(
    name='alias', # Needed to silence warnings (and to be a worthwhile package)
    url='https://github.com/psytron/alias',
    author='Mico Malecki',
    author_email='m@psytron.com',
    packages=['alias'], # Needed to actually package
    install_requires=['keycache','sysfinger','pandas','ccxt'],# Needed for dependencies
    version='0.0.8',
    license='PSYTRON', # Can be anything
    description='Alias is the container.',
    long_description=open('PYPI.md').read(),
    long_description_content_type='text/markdown'
)