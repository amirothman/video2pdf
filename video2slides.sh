#!/bin/bash

python penyedut.py $1

rm -rf image_temp/*

FILENAME="$(cat filename.tmp)"
sh split_video.sh $FILENAME

python proses_images.py > select_images.sh

rm -rf select_images/*
sh select_images.sh

