import pandas as pd

df=pd.read_csv('text_data.csv')
df['class'].value_counts()

df.head()

df['word_length'] = df['message'].str.split()
df['word_length'] = df['word_length'].str.len()
df.dropna(inplace=True)

df['word_length'].sort_values(ascending=False)

df.message.values

from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import LSTM
from keras.layers import Embedding
from keras.layers import SpatialDropout1D

MAX_WORDS = 2500
MAX_SEQUENCE_LENGTH = 355
EMBEDDING_DIM = 100

tokenizer = Tokenizer(num_words=MAX_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
tokenizer.fit_on_texts(df.message.values)
word_index = tokenizer.word_index
X = tokenizer.texts_to_sequences(df.message.values)

df.message.values[0]

X[0]

X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
Y = pd.get_dummies(df['class']).values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.10, random_state = 42)

X[0]

X_train.shape

model = Sequential()
model.add(Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=X_train.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 5
batch_size = 64

history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size,validation_split=0.1)


accr = model.evaluate(X_test,Y_test)
print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accr[0],accr[1]))


import pandas as pd

df=pd.read_csv('text_data.csv')
df.dropna(inplace=True)
df['word_length'] = df['message'].str.split()
df['word_length'] = df['word_length'].str.len()
df=df[df['word_length'] > 3]
df=df[df['class'] == 'CH3Thailand.csv']


from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import LSTM
from keras.layers import Embedding
from keras.layers import SpatialDropout1D
from keras.utils import to_categorical
import numpy as np

MAX_WORDS = 10000
MAX_SEQUENCE_LENGTH = 355
EMBEDDING_DIM = 100

tokenizer = Tokenizer(num_words=MAX_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~')
tokenizer.fit_on_texts(df.message.values)
word_index = tokenizer.word_index
X = tokenizer.texts_to_sequences(df.message.values)
X_train = []
Y_train = []

for x in X:
  for i in range(len(x)-3):
    X_train.append(x[i:i+3])
    Y_train.append(x[i+3])

X_train = np.array(X_train)
Y_train = to_categorical(Y_train, num_classes=MAX_WORDS)


Y_train


model = Sequential()
model.add(Embedding(MAX_WORDS, EMBEDDING_DIM, input_length=X_train.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(300, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(MAX_WORDS, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 50
batch_size = 100


history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size,validation_split=0.1)


def gen_text(model, tokenizer, seq_len, seed_text, num_gen_words):
    output_text = []
    input_text = seed_text
    for i in range(num_gen_words):
        encoded_text = tokenizer.texts_to_sequences([input_text])[0]
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len,truncating='pre')
        pred_word_ind = model.predict_classes(pad_encoded,verbose=0)[0]
        
        pred_word = tokenizer.index_word[pred_word_ind]
        input_text += ' '+pred_word
        output_text.append(pred_word)
    return ' '.join(output_text)

df['message']


seed_text  = "อย่า ลืม ติดตาม"
out = gen_text(model, tokenizer, seq_len=3, seed_text=seed_text, num_gen_words=10)
print('Output: '+seed_text+' '+out)



df['message']