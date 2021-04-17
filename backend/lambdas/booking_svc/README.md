# Booking Service

Manage Bookings

## Endpoints

### Create Booking

```
POST .../bookings
content-type: application/json
Authorization: <token>
{
    "name": "Sala Duza",
    "size": "5"
}
```

### Update Booking

```
PUT .../bookings/<booking_id>
content-type: application/json
Authorization: <token>
{
    "booking_id": <booking_id>,
    "user_id": 2,
    "gym_id": 4
}
```

### Delete Booking

```
DELETE .../bookings/<booking_id>
Authorization: <token>
```

### Get Bookings

```
GET .../bookings
Authorization: <token from login>
```

### Get Booking

```
GET .../bookings/<booking_id>
Authorization: <token from login>
```
