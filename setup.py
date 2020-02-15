from setuptools import find_packages, setup

import versioneer

setup(name='panel-deploy',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Easily deply panel apps via ansible',
      packages=find_packages(),
      install_requires=['ansible', 'ruamel.yaml', 'click'],
      zip_safe=False,
      entry_points='''
        [console_scripts]
        panel-deploy=panel_deploy.cli:run
      ''',
      include_package_data=True)
