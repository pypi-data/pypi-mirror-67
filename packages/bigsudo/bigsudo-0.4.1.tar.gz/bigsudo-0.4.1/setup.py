from setuptools import setup

setup(
    name='bigsudo',
    version='0.4.1',
    url='https://yourlabs.io/oss/bigsudo',
    setup_requires='setupmeta',
    keywords='automation cli ansible',
    python_requires='>=3',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bigsudo = bigsudo.console_script:cli.entry_point',
        ],
    },
)
