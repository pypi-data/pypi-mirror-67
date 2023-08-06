from setuptools import setup, find_packages

setup(
    name = 'django-lazycrud',
    version = '1.6.2',
    packages = find_packages(),
    author = 'Augusto Destrero',
    author_email = 'a.destrero@gmail.com',
    license='MIT',
    description = 'A little Django app to reduce boilerplate code at a minimum when you write class based views in a typical CRUD scenario.',
    url = 'https://github.com/baxeico/django-lazycrud',
    keywords = ['django', 'crud'],
    include_package_data = True,
    zip_safe=False,
    install_requires=[
        'django-crispy-forms>=1.6.1',
    ]
)
