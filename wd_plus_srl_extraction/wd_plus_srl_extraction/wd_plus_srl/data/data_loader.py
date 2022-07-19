import json
from os import walk
from os.path import join
from typing import List

import sys
sys.path.append("...")
import pandas as pd

from wd_plus_srl_extraction.wd_plus_srl.data.doc import Doc
from xml.etree import ElementTree

from wd_plus_srl_extraction.wd_plus_srl.data.token import Token


class IDataLoader(object):
    def __init__(self):
        pass

    def read_data_from_corpus_folder(self, corpus):
        raise NotImplementedError('Method should be overridden with data loader, example exb_data_loader')

    @staticmethod
    def get_dataloader(loader_name):
        if loader_name == "ecb":
            data_loader = EcbDataLoader()
        elif loader_name == "duc":
            data_loader = Duc2006Loader()
        elif loader_name == "text":
            data_loader = TextLoader()
        else:
            raise ValueError(
                "Argument-" + loader_name + " currently not supported, see data_loader.py for existing loaders..")
        return data_loader


class TextLoader(IDataLoader):
    def __init__(self):
        super(TextLoader, self).__init__()

    def read_data_from_corpus_folder(self, corpus):
        documents = list()
        data = pd.read_csv(r"/Users/zhusiqi/Desktop/GDI_Project/Articles.csv", encoding="utf-8")
        english_data = data[data["language"] == "eng"]
        for i in [0,1,3]:
            file = english_data["body"].loc[i]
            tokens = list()
            doc_text = ''
            sent_id = 0
            tok_inx = 0
            for line in file.split('\n'):
                if len(line.split()) == 0:
                    continue
                doc_text += line + ' '
                for token in line.split():
                    # if token in ['.', ',', '?', '!', '\'re', '\'s', 'n\'t', '\'ve',
                    #                   '\'m', '\'ll']:
                    print('Token(', sent_id,', ', tok_inx,', ', token,')')
                    tokens.append(Token(sent_id, int(tok_inx), token))
                    tok_inx += 1
                sent_id += 1
            print('Doc(', i, ', ', doc_text, ', tokens)')
            documents.append(Doc(str(i), doc_text[:-1], tokens))

        return documents

class EcbDataLoader(IDataLoader):
    def __init__(self):
        super(EcbDataLoader, self).__init__()

    def read_data_from_corpus_folder(self, corpus):
        documents = list()
        for (dirpath, folders, files) in walk(corpus):
            for file in files:
                is_ecb_plus = False
                if file.endswith('.xml'):
                    print('processing file-', file)

                    if 'ecbplus' in file:
                        is_ecb_plus = True

                    tree = ElementTree.parse(join(dirpath, file))
                    root = tree.getroot()
                    doc_id = root.attrib['doc_name']
                    tokens = list()
                    doc_text = ''
                    for elem in root:
                        if elem.tag == 'token':
                            sent_id = int(elem.attrib['sentence'])
                            tok_id = elem.attrib['number']
                            tok_text = elem.text
                            if is_ecb_plus and sent_id == 0:
                                continue
                            if is_ecb_plus:
                                sent_id = sent_id - 1

                            tokens.append(Token(sent_id, int(tok_id), tok_text))
                            if doc_text == '':
                                doc_text = tok_text
                            elif tok_text in ['.', ',', '?', '!', '\'re', '\'s', 'n\'t', '\'ve',
                                              '\'m', '\'ll']:
                                doc_text += tok_text
                            else:
                                doc_text += ' ' + tok_text

                    documents.append(Doc(doc_id, doc_text, tokens))

        print(documents)
        return documents


class Duc2006Loader(IDataLoader):
    def __init__(self):
        super(Duc2006Loader, self).__init__()

    def read_data_from_corpus_folder(self, corpus) -> List[Doc]:
        ret_docs = list()
        with open(corpus) as json_file:
            data = json.load(json_file)
            last_doc_id = None
            tok_inx = 0
            for doc_id, doc in data.items():
                tokens = list()
                for tok in doc:
                    sent_id, _, tok_text, _ = tok
                    if last_doc_id != doc_id:
                        tok_inx = 0
                        last_doc_id = doc_id
                    tokens.append(Token(sent_id, int(tok_inx), tok_text))
                    tok_inx += 1
                ret_docs.append(Doc(doc_id, "", tokens))
        return ret_docs
