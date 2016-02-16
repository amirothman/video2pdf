#!/bin/bash

ffmpeg -i $1 -vf fps=1 image_temp/image-%04d.png
