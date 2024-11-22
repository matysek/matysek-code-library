# -*- coding: utf-8 -*-
"""
Translate Android lang resources from English to Czech
using service DeepL (deepl.com).

Using official DeepL Python library `deepl`. It requires API key.
URL to obtain API key: https://www.deepl.com/en/your-account/keys

@Author: Martin Zibricky
"""

import deepl
import logging
import os
import sys

# Logging
logging.basicConfig()
logging.getLogger('deepl').setLevel(logging.DEBUG)


AUTH_KEY = os.environ["DEEPL_API_KEY"]
OUT_LANG = "CS"


def translate_text_from_file(input_path: str, output_path: str, context_path:str=None):
    """
    Translate a file, wait for response, download it and save it to output_path

    NOTE: Context is a string in output language that is not translated itself but is
          used as language context for the translation.
    """
    translator = deepl.Translator(AUTH_KEY)
    try:
        with open(input_path, 'r', encoding='utf-8') as in_file, open(output_path, 'w') as out_file:
            context_text = ''
            if context_path is not None:
                with open(context_path, 'r', encoding='utf-8') as cont_file:
                    context_text = cont_file.read()
            text = in_file.read()
            result = translator.translate_text(
                text,
                target_lang=OUT_LANG,
                formality='default',
                tag_handling='xml',
                context=context_text
            )
            out_file.write(result.text)
    except deepl.DeepLException as error:
        # Errors during upload
        print(error)


# run the program  with the following structure
# python translate_doc_deepl.py [input_path] [output_path] [context_text_path]
if len(sys.argv) == 4:
    # Also submitted context file for translation.
    translate_text_from_file(sys.argv[1],sys.argv[2], sys.argv[3])
else:
    translate_text_from_file(sys.argv[1],sys.argv[2])
