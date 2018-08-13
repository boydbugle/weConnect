#weConnect
an E-commerce review website WeConnect provides a platform that brings businesses and individuals together. This platform creates awareness for businesses and gives the users the ability to write reviews about the businesses they have interacted with.
Users get the cance to be members as well as be clients with their products being listed in the platform. Ratings can be done as stars or remarks or even both allowing a user a broad opinion and choices

## version
python3.5

## installation
clone the repo:
```
$https://github.com/boydbugle/weConnect.git
```

cd into the folder:
```
$ cd /weConnect
```


create a virtual environment for the project:
```
$ virtualenv --python=python3.5 virtualenv-name
```

activate the virtual environment:
```
$ source virtualenv-name/bin/activate
```

use virtualenv-wrapper alternative:
```
$ mkvirtualenv --python=python3.5 virtualenv-name
```

to use it:
```
$ workon virtualenv-name
```

remember to run ``` $ pip install -r requirements.txt``` to install libraries


## API endpoints
| Endpoint                                   |                  Functionality |
| ------------------------------------------ | ------------------------------ |
| `POST /api/auth/register`                  | Creates a user account         |
| `POST /api/auth/login`                     | Logs in a user                 |
| `POST /api/auth/logout`                    | Logs out a user                |
| `POST /api/auth/reset-password`            | Password reset                 |
| `POST  /api/businesses`                    | Register a busines             |
| `PUT /api/businesses/<businessId>`         | Updates a business profile     |
| `DELETE /api//businesses/<businessId>`     | Remove a business              |
| ` GET  /api/businesses`                    | Retrieves all businesses       |
| `GET  /api/businesses/<businessId>`        | Get a business                 |            
| `POST/api/businesses/<businessId>/reviews` | Add a review for a business    |
| `GET/api/businesses/<businessId>/reviews`  | Get all reviews for a business |
