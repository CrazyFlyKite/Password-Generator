from setuptools import setup, find_packages

APP = ['Password Generator/Password Generator.py']
DATA_FILES = [('assets', ['assets/images/icon.png'])]
OPTIONS = {
	'py2app': {
		'packages': find_packages(),
		'iconfile': 'assets/images/icon.png',
		'plist': {
			'CFBundleDevelopmentRegion': 'English',
			'CFBundleIdentifier': 'com.CrazyFlyKite.PasswordGenerator',
			'CFBundleVersion': '1.0',
			'HSHumanReadableCopyright': 'Copyright ©, CrazyFlyKite, All Rights Reserved'
		}
	}
}
SETUP_REQUIRES = ['py2app']
INSTALL_REQUIRES = [line.strip() for line in open('requirements.txt').readlines()]

# Setup app
if __name__ == '__main__':
	setup(app=APP, options=OPTIONS, setup_requires=SETUP_REQUIRES, install_requires=INSTALL_REQUIRES)
