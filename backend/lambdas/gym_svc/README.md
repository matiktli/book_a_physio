# Gym Service

Manage Gyms

## Endpoints

### Create Gym

```
POST .../gyms
content-type: application/json
Authorization: <token>
{
    "name": "Sala Duza",
    "size": "5"
}
```

### Update Gym

```
PUT .../gyms/<gym_id>
content-type: application/json
Authorization: <token>
{
    "gym_id": <gym_id>,
    "name": "Sala Duza",
    "size": "5"
}
```

### Delete Gym

```
DELETE .../gyms/<gym_id>
Authorization: <token>
```

### Get Gyms

```
GET .../gyms
Authorization: <token from login>
```

### Get Gym

```
GET .../gym/<gym_id>
Authorization: <token from login>
```
