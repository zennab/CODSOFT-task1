import openai
import streamlit as st 
openai.api_key = st.secrets["API_KEY"]

messages = [{"role": "system", "content": "You are a fashion advisor"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def main():
    st.title("StilestGPT")
    st.caption('Your own ***stylist*** cum ***advisor***')
    
    user_input = st.text_input(":dress:Client-", "")
    if st.button("Submit:pushpin:"):
        response = CustomChatGPT(user_input)
        st.write("Fashion Advisor:\n", response)
        st.caption("\nI HOPE IT ANSWERS YOUR DOUBT")
    
if __name__ == "__main__":
    main()