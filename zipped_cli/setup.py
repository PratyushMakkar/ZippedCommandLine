from setuptools import find_packages, setup

setup(
    name='usert',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'zipped = commands.zippedCommand:zipped',
            'login = commands.loginCommand:login'
            
        ],
    },
)