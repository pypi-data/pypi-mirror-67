import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="pyaparat",
	version="0.0.1",
	author="amirhosseing bigdelu",
	author_email="amirbig44@gmail.com",
	description="download aparat.com videos",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/amirbigg/pyaparat",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
