import setuptools

setuptools.setup(
    name='emailtools',
    version='0.0.1',
    description='Mailer tools for email campaigns.',
    author='kirkzmijewski@gmail.com',
    packages=setuptools.find_packages(),
    py_modules=['emailtools'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'emailtools = emailtools.main:cli'
        ]
    }
)