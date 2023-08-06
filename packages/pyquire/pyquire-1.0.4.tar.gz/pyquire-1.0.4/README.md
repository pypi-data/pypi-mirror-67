# Object Oriented API for Quire

A set of resources (classes) for working with [quire](https://quire.io) [API](https://quire.io/dev/api/)

All API resources available in [resources](pyquire/resources).

**Examples:**
```python
from pyquire.resources.user_resource import UserResource

print(UserResource().get_users())
# [User(oid='...', name='...', iconColor='43', image='...', ... email='...', website='')]
```

**TODO**
- [x] Create credentials class
- [x] When code received - stop server and continue work flow.

**P.S.**
> Implemented for their needs, but if there are problems, suggestions, etc. create issue in the repository.
