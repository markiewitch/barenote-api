## BareNote API 
[![Build Status](https://travis-ci.org/marszczybrew/barenote-api.svg?branch=master)](https://travis-ci.org/marszczybrew/barenote-api)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/marszczybrew/barenote-api/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/marszczybrew/barenote-api/?branch=master)

### Installation
To run this `Python` and (especially) `pip` is required. They can be downloaded [here](https://www.python.org/) or from your OS' package manager. Once installed run `make env && make install`. This will create a _Virtual environtment_ under _env_ folder and install all dependencies in that directory.

### Usage
It is recommended to run this with `debug=False` which means you should start with `make start`. There is also `make start-dev` but, as name suggests, it's there for debugging/development purposes.

### SDK
There is one [SDK in PHP](https://github.com/dzikismigol/barenote-sdk-php)

### Tests
All tests are stored in `/test`, they use [PyRestTest](https://github.com/svanoort/pyresttest/) library. So far, they are defined for the following endpoints:
 - [x] `/api/note` - it has to be decided if there will be option to choose _public_ or _private_ note type, or which will be enforced globally
 - [x] `/api/category` - individual for each user, contains a collection of user notes
 - [x] `/api/tag` - tags assignable to notes, common throughout the whole api
 - [x] `/api/login` - auth endpoint, returns JWT tokens generated with help of [PyJWT](https://github.com/jpadilla/pyjwt) library
 
### About the project
This is part of a suite of apps which I've written for Internet Programming course on my BSc Computer Science studies.
