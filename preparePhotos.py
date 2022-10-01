#!/usr/bin/env python3

import os
import shutil
import click
from progress.bar import Bar
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option("--source", '-i', help='Source folder')
@click.option("--target", '-o', help='Where to put the prepared files')
@click.option("--max-height", default=0, help='[OPTIONAL] Maximum height of the compressed photos. If unset, the original height will be conserved')
@click.option("--target-size", default=500, help='[OPTIONAL] Maximum size of compressed photos, in ko. Default = 500 ko')
@click.option("--min-quality", "init_min_quality", default=30, help='[OPTIONAL] Minimum quality of compression. Default = 30')
def prepare(source, target, max_height, target_size, init_min_quality, ):
    """
    Compress the pictures from the source folder in order
    to use them on a website. 
    """
    
    optimize_compression = True

    if not os.path.isdir(source):
        raise Exception("Source does not exist")
    if not os.path.isdir(target):
        os.mkdir(target)

    all_files = os.listdir(source)
    progressbar = Bar('Compressing photos',max=len(all_files))
    for file_name in all_files:
        file_path = os.path.join(source, file_name)
        if not os.path.isfile(file_path):
            logging.warning(f"{file_path} is a folder, not a picture")
            progressbar.next() 
            continue
        file_base_name, ext = os.path.splitext(file_name)
        ext = ext[1:]
        if ext.lower() not in ('jpg', 'jpeg', 'png'):
            shutil.copy(file_path, os.path.join(target, file_name))
            progressbar.next() 
            continue
        image = Image.open(file_path)
        image = image.convert('RGB')
        target_file = os.path.join(target, file_base_name + '.jpg')
        max_quality = 95
        min_quality = init_min_quality
        cur_quality =  (max_quality + min_quality)//2
        if max_height != 0 and image.height > max_height:
            image = image.resize((int(image.width/image.height*max_height), max_height))
        image.save(
            target_file,
            "JPEG",
            quality = cur_quality,
            progressive = True,
            optimize=optimize_compression
        )
        while max_quality-min_quality > 1:
            size = os.path.getsize(target_file)/1024
            if size < target_size:
                if cur_quality == max_quality:
                    break
                else:
                    min_quality = cur_quality
                    cur_quality = (min_quality + max_quality)//2
            else:
                if cur_quality == min_quality:
                    break
                else:
                    max_quality = cur_quality
                    cur_quality = (min_quality + max_quality)//2
            image.save(
                target_file,
                "JPEG",
                quality = cur_quality,
                progressive = True,
                optimize=optimize_compression
            )
        progressbar.next()    
    progressbar.finish()

if __name__ == '__main__':
    prepare()
