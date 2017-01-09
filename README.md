## BareNote API

#### Tests
All tests are stored in `/test`, they use [PyRestTest](https://github.com/svanoort/pyresttest/) library. So far, they are defined for the following endpoints:
 - [x] `/api/note` - it has to be decided if there will be option to choose _public_ or _private_ note type, or which will be enforced globally
 - [ ] `/api/category` - individual for each user, contains a collection of user notes
 - [ ] `/api/tag` - tags assignable to notes, common throughout the whole api
 - [x] `/api/login` - auth endpoint, returns JWT tokens generated with help of [PyJWT](https://github.com/jpadilla/pyjwt) library