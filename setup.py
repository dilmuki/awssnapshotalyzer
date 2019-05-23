from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author="Dilmurod Igamberdiev",
    author_email="dilmuki@yahoo.com",
    description="SnapshotaAlyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/dilmuki/awssnapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
    

)