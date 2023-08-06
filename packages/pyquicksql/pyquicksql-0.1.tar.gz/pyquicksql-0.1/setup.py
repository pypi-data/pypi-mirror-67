import setuptools

with open("README.md", "r") as fh:
	readme_description = fh.read()

desc = 'An out-of-the box tool for looking-up, pushing, pulling, removing MySQL, NoSQL, SQLite, MongoDB table elements in python.'

setuptools.setup(
	name = 'pyquicksql',
	packages = ['pyquicksql'],
	version = '0.1',
	license = 'MIT',
	description = desc,
	author = 'Gabriel Cordovado',
	author_email = 'gabriel.cordovado@icloud.com',
	long_description = readme_description,
	long_description_content_type = 'text/markdown',
	url ='https://github.com/GabeCordo/python-quick-sql',
	download_url = 'https://github.com/GabeCordo/python-quick-sql/archive/v_1.0.tar.gz',
	keywords = ['MYSQL', 'SQLITE', 'LOGGING'],
	install_requires = [
		'cffi',
		'pymysql',
		'sqlite3'
	],
	classifiers = [
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requries = '>=3.4',
)