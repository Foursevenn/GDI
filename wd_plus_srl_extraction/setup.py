from distutils.core import setup

setup(
    name='wd_plus_srl_extraction',
    version='1.0.0',
    packages=['wd_plus_srl_extraction', 'wd_plus_srl_extraction.utils', 'wd_plus_srl_extraction.utils.resources',
              'wd_plus_srl_extraction.dataobjs', 'wd_plus_srl_extraction.wd_plus_srl',
              'wd_plus_srl_extraction.wd_plus_srl.data', 'wd_plus_srl_extraction.wd_plus_srl.utils',
              'wd_plus_srl_extraction.wd_plus_srl.utils.resources', 'wd_plus_srl_extraction.wd_plus_srl.dataobjs',
              'wd_plus_srl_extraction.wd_plus_srl.wec_model', 'wd_plus_srl_extraction.coref_system'],
    url='',
    license='',
    author='zhusiqi',
    author_email='',
    description='',
install_requires=[
        "allennlp", #2.0.12
        "spacy==2.0.12", #2.3.0
        "scikit-learn<=0.22.2"
    ]
)
