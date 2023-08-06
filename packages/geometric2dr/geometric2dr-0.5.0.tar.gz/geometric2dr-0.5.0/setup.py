from setuptools import setup, find_packages

with open('README.md') as f:
	long_description = f.read()

setup(name="geometric2dr",
      version='0.5.0',
      description="Geo2DR: Library to build distributed representations of graphs",
      long_description = long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/paulmorio/geo2dr",
      author="Paul Scherer",
      author_email="paul.geo2dr@gmail.com",
      license="MIT",
      # packages=["geometric2dr"],
      install_requires=['numpy', 'scikit-learn', 'networkx', 'tqdm', 'ipython', 'torch', 'torchvision'],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      packages=find_packages(),
      classifiers=['Topic :: Scientific/Engineering :: Artificial Intelligence',
      				'License :: OSI Approved :: MIT License',
      				'Natural Language :: English',
      				'Programming Language :: Python :: 3.6',
      				'Operating System :: OS Independent'],
      zip_safe=False
      )
