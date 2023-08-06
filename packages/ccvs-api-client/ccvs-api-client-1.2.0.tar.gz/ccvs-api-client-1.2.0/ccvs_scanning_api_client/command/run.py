# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import argparse
import json

from ccvs_scanning_api_client.command import analysis


def main():
    parser = argparse.ArgumentParser(
        description='Find vulnabilities in docker images.')

    parser.add_argument(
        '-i', '--image_tag',
        help='docker image: docker-registry.exemple.com/image:tag',
        dest='image_tag',
        required=True)
    parser.add_argument(
        '-w', '--whitelist',
        help='yaml file with whitelist',
        dest='whitelist_file',
        required=False)
    parser.add_argument(
        '-o', '--output',
        help='file name to save results',
        dest='output_file',
        required=False)

    image_tag = parser.parse_args().image_tag
    output_file = parser.parse_args().output_file
    whitelist_file = parser.parse_args().whitelist_file

    analysis_result = analysis.analysis(image_tag, whitelist_file)
    results = analysis.summary(analysis_result)

    if output_file:
        save_json(results, output_file)
    else:
        print(json.dumps(results))  # noqa


def save_json(results, output_file):
    analysis_result_file = open(output_file, 'w')
    analysis_result_file.write(json.dumps(results))
    analysis_result_file.close()


if __name__ == '__main__':
    main()
