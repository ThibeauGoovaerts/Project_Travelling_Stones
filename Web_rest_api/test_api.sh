#!/bin/bash

http -b POST http://vps-732282ba.vps.ovh.net:8888/api/token username=thibeau password=user123

http -b GET http://vps-732282ba.vps.ovh.net:8888/api/personne Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"

http -b GET http://vps-732282ba.vps.ovh.net:8888/api/calloux Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"

http -b GET http://vps-732282ba.vps.ovh.net:8888/api/decouverte Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"

http -b GET http://vps-732282ba.vps.ovh.net:8888/api/adresse Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"

http -b GET http://vps-732282ba.vps.ovh.net:8888/api/pays Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"

http -b POST http://vps-732282ba.vps.ovh.net:8888/api/pays nom=portugal Authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NTg2OTk2LCJpYXQiOjE2NzQ1ODMzOTYsImp0aSI6IjQxNGVkNWQ3NGRmMjRjODVhODc1NGE5MjRhODA4NmU4IiwidXNlcl9pZCI6InRoaWJlYXUifQ.hHoNSpMKsNqQbf_cDQerVq5u5p24WPoR_ppj6ZfEPAw"