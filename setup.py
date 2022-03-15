import setuptools

with open('README.md', 'r', encoding = ' utf-8') as rm:
    long_description = rm.read()

setuptools.setup(
    name = 'pjnturtle',
    version = '0.0.32',
    author = 'Reto Krummenacher',
    author_email = 'reto.krummenacher@unibas.ch',
    description = 'Simple python turtle for Jupyter Notebooks',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/RetoKrummenacher/PJNturtle',
    license = 'Apache 2.0',
    packages = ['pjnturtle', 'pjnturtle.common','pjnturtle.resources'],
    package_data = {'pjnturtle': ['resources/*.png','resources/*.ttf']},
    install_requires = ['Pillow'],    
)

