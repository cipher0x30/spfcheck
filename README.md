# SPF Record Checker

Checks if a domain has valid SPF records.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
This requires the following:

- [pyspf](https://github.com/sdgathman/pyspf)
- [pydns](http://pydns.sourceforge.net/) or [dnspython](http://www.dnspython.org/)

### Installing


0. Clone this repository

	```
	git clone https://github.com/cipher0x30/spfcheck
	```
1. Navigate to your destination folder.

	```
	cd spfcheck
	```

2. Install the requirements

	```
	pip install -r requirements.txt
	```

## Usage

0. Navigate to your destination folder

	```
	cd spfcheck
	```
1. Make it executable

	```
	chmod +x spfcheck.py
	```

	```
	./spfcheck
	```

	or just run it the normal way;

	```
	python spcheck.py
	```

2. Enter your target domain

	```
	Hostname: google.com 
	```

	*NOTE: The domain is everything to the right of the '@' in the e-mail address.*


## Author/s

* **cipher0x30** - *Initial work* 

See also the list of [contributors](https://github.com/cipher0x30/spfcheck/contributors) who participated in this project.

## License

This project is free to distribute, modify and use with the condition that credit is provided to the creator [cipher0x30](https://github.com/cipher0x30) and is not for commercial use.

