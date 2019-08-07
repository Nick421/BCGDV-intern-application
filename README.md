# BCGDV-intern-application
Code for intern submission 

# Python solution
The solution is in BCGDV.py, self explainatory.

# Curl solution
Below is how I did it before the python code was written. (Sorry for submitting twice)
## GET request
```
curl -k -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET https://interns.bcgdvsydney.com/api/v1/key
```
## POST request

```
curl -v -k -d '{"name":"Niravit Theng", "email":"niravit.theng@gmail.com"}' -H "Content-Type: application/json" -X POST https://interns.bcgdvsydney.com/api/v1/submit?apiKey=ec738006-6aa1-499a-abc7-299f2bd4db09
```
