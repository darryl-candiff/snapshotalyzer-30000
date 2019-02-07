from setuptools import setup

setup(
    name='snapshotanalyzer-30000',
    version='0.1',
    author="Darryl Candiff",
    author_email='darryl@ccservices.nl',
    summary="SnapshotAyzer 30000 is a demo tool to manage AWs EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/darryl-candiff/snapshotalyzer-30000",
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
