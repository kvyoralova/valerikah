import streamlit as st
from PIL import Image
from gtts import gTTS
from googletrans import Translator
translator = Translator()
from transliterate import translit, get_available_language_codes

st.title("Італійський розмовник для дітей - Итальянский разговорник для детей")
purposeuk = """ -  UK: Цей додаток має на меті допомогти українським дітям, як російською, так і українською мовою, вивчити та використовувати деякі корисні фрази італійською"""
st.write(purposeuk)
st.write(""" -  RU: Это приложение нацелено на то, чтобы помочь украинским и русскоязычным детям выучить и использовать некоторые полезные фразы на итальянском языке""")
purpose = st.checkbox('Click here if you want to know the purpose of this app in another language')
if purpose:
  lang = st.selectbox("Insert the code of a language in which you want to know the purpose of the app:", ('en', 'de', 'it'))
  translation = translator.translate(purposeuk, dest=lang)
  purposetext = translation.text
  st.write(purposetext)
else:
  pass


language = st.radio( "Виберіть мову - Выберите язык" , ('Русский', 'Yкраїнський'))

if language == 'Русский':
  placechoice = st.selectbox("Куда ты хочешь пойти сегодня? Bыбери одно из указанных мест:", ('Площадка для игр', 'Школа', 'Магазин канцтоваров'))

cola, colb, colc, cold = st.columns(4)
with cola:
  st.subheader("Полезные выражения")
with colb:
  st.subheader("Итальянский перевод")
with colc:
  st.subheader("Вот как это звучит")
with cold:
  st.subheader("На кириллице")
      
phrases_ru = {'Площадка для игр': [{'Пойдем в парк' : 'Andiamo al parco'},
                                   {'Давай играть в прятки' : 'Giochiamo a nascondino'},
                                   {'Давай покатаемся на качелях' : "Andiamo sull'altalena"},
                                   {'Пойдем на горку' : 'Andiamo sullo scivolo'},
                                   {'Давайте прыгать на скакалке' : 'Saltiamo la corda'}],
              'Школа': [{'Потом поиграем вместе?' : 'Dopo giochiamo insieme?'},
                         {'Давай сделаем пазл' : 'Facciamo un puzzle'},
                         {'Давай рисовать' : 'Disegnamo?'},
                         {'Пойдём в сад?' : 'Andiamo in giardino?'},
                         {'Могу ли я взять твой фломастер?' : 'Mi presti il tuo pennarello?'}],
              'Магазин канцтоваров': [{' Добрый день' : 'Buongiorno'},
                                      {'Мне нужны тетради' : 'Mi servirebbero dei quaderni'},
                                      {'Мне нужна линейка' : 'Avrei bisogno di un righello'},
                                      {'Мне нужны цветные карандаши' : 'Mi servirebbero le matite colorate'},
                                      {'Сколько это стоит?' : 'Quanto costa?'}]
                        }



phrase_list_place = phrases_ru[placechoice]
for phrasecouple in phrase_list_place:
  for rus, ita in phrasecouple.items():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
      st.write(rus)
    with col2:
      translation = translator.translate(rus, dest= 'it')
      translated_text= translation.text
      if translated_text != ita:
        translated_text = ita
      else:
        pass
      st.write(translated_text)
    with col3:
      tts1=gTTS(translated_text, lang = 'it')
      tts1.save('your_file.mp3')
      audio_file = open('your_file.mp3', 'rb')
      st.audio(data=audio_file, format="audio/mp3", start_time = 0)
    with col4:
      transliterated_text = translit(translated_text, 'ru')
      st.write(transliterated_text)
