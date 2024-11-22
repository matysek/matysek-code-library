# -*- coding: utf-8 -*-
"""
Translate Android lang resources from English to Czech
using Google Translate (translate.google.com).

It uses only the free google translate service with its limitations.
Using library `googeltrans-modified`. Original library is unmaintained.

pip install googletrans-modified


@Author: Martin Zibricky
"""

import googletrans
import logging
import os
import sys

# Logging
logging.basicConfig()
logging.getLogger('googletrans').setLevel(logging.DEBUG)


OUT_LANG = "CS"


def translate_text_from_file(input_path: str, output_path: str):
    """
    Translate a file, wait for response, download it and save it to output_path
    """
    translator = googletrans.Translator()
    with open(input_path, 'r', encoding='utf-8') as in_file, open(output_path, 'w') as out_file:
        text = in_file.read()
        result = translator.translate(
            text,
            dest=OUT_LANG,
        )
        out_file.write(result.text)


# run the program  with the following structure
# python translate_doc_google.py [input_path] [output_path]
translate_text_from_file(sys.argv[1],sys.argv[2])
