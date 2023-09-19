from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')
setup(
    name = 'NCHU_nlptoolkit',
    packages=['NCHU_nlptoolkit'],
    package_dir={'NCHU_nlptoolkit':'NCHU_nlptoolkit'},
    package_data={'NCHU_nlptoolkit':['dictionary/*', 'cut/*', 'scripts/dump2es.py']},
    version = '2.0.5',
    description = 'nlplab dictionary, stopwords module',
    author = ['davidtnfsh', 'CYJiang0718','dancheng'],
    author_email = 'nlpnchu@gmail.com',
    url = '',
    download_url = '',
    keywords = ['NCHU_nlptoolkit', 'jieba', 'dictionary', 'stopwords'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'jieba',
        'nltk',
        'numpy'
    ],
    zip_safe=True,
    scripts=['NCHU_nlptoolkit/scripts/dump2es.py'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
