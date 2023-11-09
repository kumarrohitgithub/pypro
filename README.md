# pypro
Note: This sample doesn't use any authentication token, only available for actors.

Based on Python and modules used django, djangorestframework

How to use RestAPI?
**Host** : http://20.193.135.123:8000

**GET** actors/get/

**POST** actors/create/
Body type form - 
{
  "first_name":String, 
  "last_name":String
}

**PUT** actors/update/{{id}}/
{
  "first_name":String, 
  "last_name":String
}

**DELETE** actors/{{id}}/delete/

