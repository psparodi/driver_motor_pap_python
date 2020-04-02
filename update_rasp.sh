#!/bin/bash


#DIR='pi@10.2.41.38'
#DIR='pi@192.168.0.143'
DIR='pi@192.168.0.222'

eval scp motor.py ${DIR}:;
eval scp main.py ${DIR}:;
