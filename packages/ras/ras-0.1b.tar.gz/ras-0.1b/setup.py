from distutils.core import setup
setup(
  name = 'ras',         # How you named your package folder (MyLib)
  packages = ['ras'],   # Chose the same as "name"
  version = '0.1b',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Algo standard rethinkdb api wrapper',   # Give a short description about your library
  author = 'Techa Gal',                   # Type in your name
  author_email = 'Techa.G@mail.com',      # Type in your E-Mail
  url = 'https://github.com/techagal/rdb-sample',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/techagal/rdb-sample/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Algo', 'SS&C Algo', 'Algo RethinkDB', 'Algo RAS', 'RethinkDB'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'rethinkdb',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',      #Specify which pyhton versions that you want to support
  ],
)