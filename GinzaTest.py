import spacy

nlp: spacy.Language = spacy.load('ja_ginza')

#text を　Doc　クラスに変換する
text: str = '錦織圭選手はテニスが大好きです'
doc: spacy.tokens.doc.Doc = nlp(text)


#DocクラスはTokenクラスのイテレーターになっている
for token in doc:
    print(token.text, type(token))