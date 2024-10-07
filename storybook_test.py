import os

import streamlit as st
from openai import OpenAI


my_secret = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=my_secret)


#Story generator method
def story_gen(prompt):

  system_prompt = """
  You are a world renowned 50 years experienced children storyteller. 
  You will be given a concept to generate a story suitable for ages 5 to 7 years old.
  """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system",
          "content": system_prompt},
          {"role":"user",
          "content":prompt}
      ],
      temperature = 1.3,
      max_tokens = 200
  )

  return response.choices[0].message.content


#Cover prompt generator method
def cover_gen(prompt):

  system_prompt = """
  You will be given a children story book. 
  Generate a prompt for a cover art that is suitable and shows off the story themes.
  The prompt will be send to dall e 2.
  """

  response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[
          {"role": "system",
          "content": system_prompt},
          {"role":"user",
          "content":prompt}
      ],
      temperature = 1.3,
      max_tokens = 200
  )

  return response.choices[0].message.content


#Image generator method
def image_gen(prompt):
  response = client.images.generate(
      model = 'dall-e-2',
      prompt = prompt,
      size = '256x256',
      n=1,
  )

  return response.data[0].url


#Stoorybook method
def storybook(prompt):
  story = story_gen(prompt)
  cover = cover_gen(story)
  image = image_gen(cover)


  st.write('image') 
  st.write('story')

st.title("Storybook Generator for Awesome Kids")
st.divider()

prompt = st.text_area("Enter your story idea here")

if st.button(label="Generate Storybook"):
  story = story_gen(prompt)
  cover = cover_gen(story)
  image = image_gen(cover)

  st.balloons()
  st.image(image) 
  st.write(story)
