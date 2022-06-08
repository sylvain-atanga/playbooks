#! /bin/bash

for i in playbook*
do
	ansible-playbook $i
done
