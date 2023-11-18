import openai
import streamlit as st
import time
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
PROMPT = os.getenv("PROMPT")
client = openai.OpenAI()

PROMPT = "Can you give actionable ideas related to the elements in the design to increase conversion & Reduce Bounce Rate. Give around 7 ideas."


st.set_page_config(
    page_title="Actionable Ideas for Better Conversion Rate",
    page_icon=":robot:"
)

st.title("AI UI/UX Conversion Advisor")
st.markdown('''
## Actionable Ideas for your Hero Section to Improve Conversion & Reduce Bounce Rate.
Please do Try again, if you don't get results at once.
''')


def gpt4v(screenshot_url):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": screenshot_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=500,
    )
    return response.choices[0].message.content


def check_website_url(text):
    if text.startswith("http"):
        return True
    if len(text.split()) > 1:
        return False
    else:
        return True


website_input = st.text_input("Website/Page URL", key="website")
if st.button("Submit", type="primary"):
    if website_input:
        placeholder = st.empty()
        if check_website_url(website_input):
            # change it later to website_input
            if not website_input.startswith('http'):
                website_input = "https://" + website_input
            url = 'https://image.thum.io/get/auth/69444-uiux/' + \
                website_input  # "https://screenshotone.com/images/stripe.webp"

            placeholder.text("loading the site...")
            time.sleep(4)  # load the screenshot
            placeholder.text("Finding Improvement Ideas for " + website_input)
            content = gpt4v(url)
            placeholder.empty()
            st.subheader("Improvement Ideas for " + website_input +
                         " ...", divider='rainbow')
            st.image(url)
            st.write(content)
        else:
            st.write("Please provide a valid website url")
    else:
        st.write("Please provide a valid website url")
