import spacy
from spacy import displacy

# Languageクラス 変数名をnlpで宣言するのが一般的（spaCy推奨）
spacy.Language = spacy.load('ja_ginza')