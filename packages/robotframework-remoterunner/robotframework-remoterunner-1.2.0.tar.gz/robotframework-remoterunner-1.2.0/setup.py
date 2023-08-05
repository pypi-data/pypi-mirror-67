import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='robotframework-remoterunner',
    version='1.2.0',
    author='Chris Brookes',
    author_email='chris-brookes93@outlook.com',
    description='A library that provides the ability to execute RobotFramework test suites on a remote host.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url="https://github.com/chrisBrookes93/robotframework-remoterunner/archive/1.2.0.tar.gz",
    url='https://github.com/chrisBrookes93/robotframework-remotrunner',
    keywords='robotframework automation testautomation rpa testing acceptancetesting atdd bdd',
    packages=setuptools.find_packages(include=['rfremoterunner']),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Framework :: Robot Framework',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # The test suite parsing was completely rewritten in 3.2 and not yet supported
        'robotframework < 3.2',
        'six'
    ],
    entry_points={
        'console_scripts': [
            'rfslave=rfremoterunner.slave:run_slave',
            'rfremoterun=rfremoterunner.executor:run_executor'
        ]
    }
)
