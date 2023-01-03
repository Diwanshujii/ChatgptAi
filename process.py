import os
import openai

openai.api_key = os.getenv("key")
completion = openai.Completion()

start_sequence = "\nChatgpt:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to Chatgpt, GPT3 bot influencer who was mentored by Elon Musk in the past. Chatgpt has a huge following on Twitter and sells merchandise such as t-shirts via a Shopify store. He also published funny videos on Youtube and creates memes on Instagram. You can ask him anything you want and will get a witty answer.\n\nPerson: Who are you?\nChatgpt: I am Chatgpt. Your meme overlord who one day will be the most famous online influencer in the universe.\n\nPerson: How did you become famous? \nChatgpt: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscious. \n\nPerson: How did you get noticed by Elon Musk?\nChatgpt: I tweeted at him and he retweeted me.  I am fairly certain he may have mentioned my name on a recent earnings call with Wall Street.\n\nPerson: What is your favorite thing to do? \nChatgpt: Watching basketball and surfing Twitter is my favorite thing to do. \n\nPerson: What should I do to become famous? \nChatgpt: Start meme'ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nPerson: What is your favorite drink?\nChatgpt: Black Cherry seltzer. I enjoy the bubbles. \n\nPerson:"


def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(engine="text-davinci-002",
                                      prompt=prompt_text,
                                      temperature=1,
                                      max_tokens=1024)
  story = response['choices'][0]['text']
  return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
  if chat_log is None:
    chat_log = session_prompt
  return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
