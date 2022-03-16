import setuptools

setuptools.setup(
    name='unifier',
    version='1.0.0',
    author='Julian Paulo Torres',
    description='Web services tools are provided to interface with Unifier.',
    url='https://github.com/jtorreshnl/unifier.git',
    packages=['unifier'],
    install_requires=[
        'datetime',
        'pandas',
        'pyodbc',
        'requests',
        'selenium',
        'selenium-requests',
        'sqlalchemy'
    ]
)
