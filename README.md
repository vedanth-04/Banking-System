# CREATE A STREAMLIT APP USING FIRESTORE DATABASE
![image](https://github.com/user-attachments/assets/2c2b80f0-dd58-4aa5-a231-9d95de36e233)

# Prerequisites
1.[Latest python IDLE version](https://www.python.org/downloads/)
2.[Install visual studio code](https://code.visualstudio.com/download)

## What is Streamlit?

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you’ve created an app, you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app.

### Why choose Streamlit?

- **Simple and Pythonic:** Write beautiful, easy-to-read code.
- **Fast, interactive prototyping:** Let others interact with your data and provide feedback quickly.
- **Live editing:** See your app update instantly as you edit your script.
- **Open-source and free:** Join a vibrant community and contribute to Streamlit's future.

- ## Installation

Open a terminal and run:

```bash
$ pip install streamlit
$ streamlit hello
```

If this opens our sweet _Streamlit Hello_ app in your browser, you're all set! If not, head over to [our docs](https://docs.streamlit.io/get-started) for specific installs.

The app features a bunch of examples of what you can do with Streamlit. Jump to the [quickstart](#quickstart) section to understand how that all works.

<img src="https://user-images.githubusercontent.com/7164864/217936487-1017784e-68ec-4e0d-a7f6-6b97525ddf88.gif" alt="Streamlit Hello" width=500 href="none"></img>

## Quickstart

### A little example

Create a new file `streamlit_app.py` with the following code:
```python
import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
```

Now run it to open the app!
```
$ streamlit run streamlit_app.py
```

<img src="https://user-images.githubusercontent.com/7164864/215172915-cf087c56-e7ae-449a-83a4-b5fa0328d954.gif" width=300 alt="Little example"></img>
