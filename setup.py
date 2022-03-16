import setuptools

with open('README.md', 'r', encoding = ' utf-8') as rm:
    long_description = rm.read()

setuptools.setup(
    name = 'pjnturtle',
    version = '1.0.0',
    author = 'Reto Krummenacher',
    author_email = 'reto.krummenacher@unibas.ch',
    description = 'Simple Turtle Graphics in Python for Jupyter Notebooks',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/RetoKrummenacher/PJNturtle',
    
      # BSD 3-Clause License:
      # - http://choosealicense.com/licenses/bsd-3-clause
      # - http://opensource.org/licenses/BSD-3-Clause

    license='BSD',
    packages = ['pjnturtle', 'pjnturtle.common','pjnturtle.resources'],
    package_data = {'pjnturtle': ['resources/*.png','resources/*.ttf']},
    install_requires = ['Pillow'],    
)

