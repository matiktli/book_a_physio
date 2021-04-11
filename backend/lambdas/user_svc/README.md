# User Service

User and Security Service basically

## Endpoints

### Register

```
POST .../users/register
content-type: application/json
{
    "email": "user@user.pl",
    "password": "password"
}
```

### Login

```
POST .../users/login
content-type: application/json
{
    "email": "user@user.pl",
    "password": "password"
}
```

### Authorize Token

```
GET .../users/authorize?token=<token>
```

### Curent User

```
POST .../users/me
Authorization: <token from login>
```
