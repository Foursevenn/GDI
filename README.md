## GDI_Project

#### A. Directly-related Resources

Papers:

https://arxiv.org/pdf/2109.11621.pdf

Dataset:

DUC 2006 MDS dataset: D0601, D0602, D0606, D0608, D0617, D0629.

Result:

found the *Statements* facet-values rather lengthy and less useful.

Github repo:

https://github.com/BIU-NLP/iFACETSUM

App demo:

https://biu-nlp.github.io/iFACETSUM/WebApp/client	

#### B. Setup Steps

#### a. 

git clone this repo

Install python>=3.6



#### b. 

Open iFACETSUM dir in pycharm (it's better make a new venv and install r)

Open two terminals

```markdown
#### Set up the server
cd to the GDI/iFACETSUM dir
1. Run `pip install -r requirements.txt`
2. Run `python -m spacy download en_core_web_md`
3. From inside python, run `import nltk` and then `nltk.download('punkt')`
4. Run `python WebApp/server/app.py`

#### Set up the client (node)
1. Run `cd GDI/iFACETSUM/WebApp/client`
2. Run `npm install`
3. Run `npm start`
4. Open the url `http://localhost:3000`
```



#### c.

##### 1. Open wd-plus-srl-extraction dir in pycharm

```markdown
### WEC CD Coreference
`coref_wec_model.py` Generate within document and cross-document coreference using AllenNlp coref and WEC-Eng models.<br/>
This script has been used to generate the entity cross-document coreference facets in [IFacetSum](https://github.com/BIU-NLP/iFACETSUM).<br/>   

run:
    python src/coref_wec_model.py --input_file=input/Steroid_Use_docs_formatted.json --output_file=output/Steroid_allen_wd_coref_duc.json --loader=duc --model_file=model/wec_model --cuda=False
```

##### 2. edit the config on the top right of pycharm UI

**Script Path:**

GDI/iFACETSUM/wd_plus_srl_extraction/wd_plus_srl_extraction/wd_plus_srl/coref_wec_model.py

**Parameters:**

--input_file=

/Users/zhusiqi/Desktop/GDI_Project/wd_plus_srl_extraction/input/Steroid_Use_docs_formatted.json

--output_file=/Users/zhusiqi/Desktop/GDI_Project/wd_plus_srl_extraction/output/Steroid_allen_wd_coref_duc.json

--loader=duc

--model_file=/Users/zhusiqi/Desktop/GDI_Project/wd_plus_srl_extraction/model/wec_model

--cuda=False

**Working Dir:**

GDI/iFACETSUM/wd_plus_srl_extraction/wd_plus_srl_extraction/wd_plus_srl

##### 3. press the run button



i impelement a TextLoader in wd_plus_srl_extraction/wd_plus_srl/data/data_loader.py

if we want to get the event core firectly from our own resource articles, change the 'loader' in the parameters to 'text'

However, this dataloader is not dealing with the symbols. this can be further improved



#### C. 

This readme is subject to change

I also put EBC+ corpus and a jupyter notebook into the repo. for now, please just ignore it.
