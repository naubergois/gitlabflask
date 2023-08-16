#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime


def check_post_integrity(post_content):
    required_fields = ['title', 'subtitle', 'author', 'author_image', 'date', 'image', 'permalink', 'tags',
                       'shortcontent']

    print("Workdir: " + os.getcwd())

    # check if all required fields are present in post_content keys with a not null value
    for field in required_fields:
        if field not in post_content.keys():
            print("ERROR: Missing field: " + field)
            return False
        elif not post_content[field]:
            print("ERROR: Missing value for field: " + field)
            return False


    # check date is in the format %B %d, %Y
    try:
        datetime.strptime(post_content['date'], '%B %d, %Y')
    except ValueError:
        print("ERROR: Incorrect date format, should be Month Day, Year")
        return False

    tags = post_content['tags'].strip()
    tag_list = tags.split(',')
    # checks that each tag is a word without spaces or punctuation
    for tag in tag_list:
        if not tag.isalnum():
            print("ERROR: Incorrect tag format, should be a word without spaces or punctuation")
            return False


    # check image name is in app/static/assets/blog-images
    image_path = os.path.join('static', 'assets', 'blog-images', post_content['image'])
    if not os.path.exists(image_path):
        print("ERROR: Image file does not exist, path: " + image_path)
        return False

    # check author_image name is in static/assets/blog-images
    author_image_path = os.path.join('static', 'assets', 'blog-images', post_content['author_image'])
    if not os.path.exists(author_image_path):
        print("ERROR: Author image file does not exist, path: " + author_image_path)
        return False

    return True


def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    post_data = {}

    # Iterate over each line in the file
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        if not line:
            continue  # Skip empty lines

        if ':' not in line:
            continue  # Skip lines without a colon separator

        key, value = line.split(':', 1)  # Split the line into key and value

        key = key.strip().lower()  # Convert key to lowercase and remove whitespace
        value = value.strip()  # Remove leading/trailing whitespace

        post_data[key] = value

    # for key in post_data:
    #     print(key, ':', post_data[key])

    return post_data


def main():
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            print(f'file_path: {file_path}')
            print("Processing file:", file_path)
            post_content = parse_file(file_path)
            integrity_check = check_post_integrity(post_content)

            if integrity_check:
                print("The post is valid.")
            else:
                print("ERROR: The post is not valid.")
                exit(1)
    else:
        print("ERROR: No file paths provided.")
        exit(1)


if __name__ == '__main__':
    main()
