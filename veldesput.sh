#!/bin/bash

curl -H "Content-Type: application/json" -d '{"value": 100}' -X PUT http://127.0.0.1/velocityDesired
