#!/bin/bash

# get all images that start with localhost:32000, output the results into image_ls file
sudo microk8s ctr images ls name~='localhost:32000' | awk {'print $1'} > image_ls