#!/bin/bash

python3 ./main.py | flask --app ./controller/controladorFlask.py run