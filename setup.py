"""
Setup script for `tcli-oncall`
"""

from setuptools import setup

setup(
    name='tcli-oncall',
    version='0.1.0',
    packages=['tcli_oncall'],
    entry_points='''
        [tcli.plugins]
        oncall=tcli_oncall.plugin:oncall
    ''',
)
