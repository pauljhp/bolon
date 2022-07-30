import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils import SessionState
import datetime as dt
import streamlit.components.v1 as components
from images import images_df

TODAY = dt.datetime.today().date()

st.set_page_config(page_title="Bolon <3 <3", page_icon=":pig:", 
    layout="centered", initial_sidebar_state="auto", 
    menu_items=None)
JJ_NEXT_HINT = ":dog: Hit next when you are done! Woof Woof!"
############### for pagination ##################
last_page = 100

session_state = SessionState.get(page_number = 0)
prev, home ,next = st.columns(3, gap='large')

if next.button("Next"):
    
    if session_state.page_number + 1 > last_page:
        session_state.page_number = 0
    else:
        session_state.page_number += 1

if prev.button("Back"):

    if session_state.page_number - 1 < 0:
        session_state.page_number = last_page
    else:
        session_state.page_number -= 1

if home.button("Home"):

    session_state.page_number = 1

############### for pagination ##################

st.title(":heart: :heart: :heart:\nHappy Birthday Bolon :pig: ! \n\n:heart: :heart: :heart:")

if session_state.page_number == 1:
    
    st.markdown("## :boom: First thing first")
    st.markdown("""
    This is your 30 year birthday, and I'm sure you feel complicated, maybe even scared. \n
    And that's why I'm going to make this birthday special. \n
    It's not just about making you feel good and loved, but also, I truly think you are a wonderful person with great potential. \n
    Let's not think about all that first and focus on your birthday today, shall we? \n
    :pig: :pig: :pig: :paw_prints: :paw_prints: :paw_prints: \n
    \n""")
    st.caption(
    ":loudspeaker: Hint from JJ :dog: : Hit next to see what's next! Woof Woof!!"
    )

else:
    st.subheader(":point_right: First, you will have to make a few choices")
    choice1_options = {
        0: 'Present first!',
        1: 'Have some more fun first!', 
        2: "Let's go down memory lane first!"
    }
    choice1 = st.radio(label=":point_right: What would you like to see first?", 
        options=list(choice1_options.values()),
        index=0,)
    st.caption(JJ_NEXT_HINT)
    if session_state.page_number >= 3:
        if choice1 == choice1_options.get(0):
            if session_state.page_number >= 4:
                st.markdown(f"""You selected {choice1_options[0]}. 
                Sure, let's do presents first. You have to make a few choices still though!""")
                choice20_options = {
                    0: "Something exciting!",
                    1: "Something quirky!",
                    2: "I'll pass. Let me go back!"
                }
                choice20 = st.radio(label="What kind of of present would you like to receive?",
                    options=list(choice20_options.values()),
                    index=1)
                st.caption(JJ_NEXT_HINT)
                if session_state.page_number >= 5:
                    if choice20 == choice20_options.get(0):
                        st.write("Sure, let's do something exceiting. How about something you've always wanted?")
                        st.write("Find Bolon for assistance and show him the following QR code:\n")
                    elif choice20 == choice20_options.get(1):
                        st.write("Sure, let's do something quirky. Bolon is best at this. Show him the following QR code:")
                    elif choice20 == choice20_options.get(2):
                        session_state.page_number = 1

        elif choice1 == choice1_options.get(1):
            st.markdown(f"""You selected {choice1_options[1]}. 
            Sure, let's have some fun first. Here's are some funny videos:""")
            choice21_options = {
                0: "That's it? You suck!",
                1: "Let me go back!",
            }
            choice21 = st.radio(label="What do you do now?",
                options=list(choice21_options.values()),
                index=1)
        
        elif choice1 == choice1_options.get(2):
            st.markdown(f"""You selected {choice1_options[2]}. 
            Sure, let's go down memory lane before officially turning 30. """)

            choice22 = st.date_input(label="How far back do you want to go?",
                value=dt.date(2015, 3, 11),
                min_value=dt.date(1992, 7, 31),
                max_value=TODAY,
                )
            if session_state.page_number >= 3:
                st.write(f"Ok! Let's go back from {choice22.strftime('%Y-%m-%d')}. Here you go...")
                images = images_df.query("filedate>=@choice22")
                
                i = session_state.page_number - 3
                print(i)
                if i in range(len(images)):
                    row = images.iloc[i]
                    st.text(f"{row.filedate.strftime('%B %d, %Y')}")
                    url = row.url
                    components.html(f"""{row.filename}
                    <img src="{url}" width="300" height="200" style="vertical-align:bottom">""",
                    )
                    if i < len(images) - 1:
                        st.caption(
                            ":loudspeaker: Hint from JJ :dog: : Hit next to see what's next! Woof Woof!!"
                            )
                    else:
                        st.caption("This is the end of the journey!")
        
        else: raise NotImplementedError
