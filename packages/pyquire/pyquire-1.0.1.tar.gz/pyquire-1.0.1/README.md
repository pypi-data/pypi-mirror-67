# Object Oriented API for Quire

A set of resources (classes) for working with [quire](https://quire.io) [API](https://quire.io/dev/api/)

All API resources available in [resources](pyquire/resources).

**Examples:**

Before queries you need initialize Credential object (he singleton). 

```python
from pyquire.credentials import Credentials
from pyquire.resources.user_resource import UserResource

# Credentials.initialize(
#    set_file="./conf.json"
# )
# or
# Credentials.initialize(
#     access_token="ACCESS_TOKEN",
#     expires_in=3599,
#     refresh_token="REFRESH_TOKEN",
#     client_id="CLIENT_ID",
#     client_secret="CLIENT_SECRET"
# )
# or
Credentials.initialize( 
     client_id="CLIENT_ID", 
     client_secret="CLIENT_SECRET", 
     set_file="./conf.json"
) 
print(UserResource().get_users())
# [User(oid='...', name='...', iconColor='43', image='...', ... email='...', website='')]
```

**TODO**
- [x] Create credentials class
- [x] When code received - stop server and continue work flow.

**P.S.**
> Implemented for their needs, but if there are problems, suggestions, etc. create issue in the repository.
