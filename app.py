import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils import SessionState, make_qrcode
import datetime as dt
import streamlit.components.v1 as components
from images import images_df
from videos import video_urls
from texts import ending_text
from copy import deepcopy


TODAY = dt.datetime.today().date()

st.set_page_config(page_title="Bolon <3 <3", page_icon=":pig:", 
    layout="centered", initial_sidebar_state="auto", 
    menu_items=None)
JJ_NEXT_HINT = ":dog: Hit next when you are done! Woof Woof! (you may have to hit next twice)"
############### for pagination ##################
last_page = 100

session_state = SessionState.get(page_number = 0)
prev, home ,next = st.columns(3, gap='large')
current_page = session_state.page_number

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

    session_state.page_number = 0

############### for pagination ##################

st.title(":heart: :heart: :heart:\nHappy Birthday Bolon :pig: ! \n\n:heart: :heart: :heart:")
cur_p = 0
if session_state.page_number < 1:
    
    st.markdown("## :boom: First thing first")
    st.markdown("""
    This is your 30th birthday, and I'm sure you feel complicated, maybe even scared. \n
    And that's why I'm going to make this birthday special. \n
    It's not just about making you feel good and loved, but also, I truly think you are a wonderful person with great potential. \n
    Let's not think about all that first and focus on your birthday today, shall we? \n
    :pig: :pig: :pig: :paw_prints: :paw_prints: :paw_prints: \n
    \n""")
    st.caption(
    ":loudspeaker: Hint from JJ :dog: : Hit next to see what's next! Woof Woof!!"
    )

else:
    cur_p = 0
    st.markdown("## :point_right: First, you will have to make a few choices")
    choice1_options = {
        0: 'Present first!',
        1: 'Have some more fun first!', 
        2: "Let's go down memory lane first!",
        3: "Take me to my Bolon coupons"
    }
    choice1 = st.radio(label="What would you like to see first?", 
        options=list(choice1_options.values()),
        index=0,)
    st.caption(JJ_NEXT_HINT)
    
    if current_page >= cur_p:
        if choice1 == choice1_options.get(0):
            cur_p += 1
            # print(cur_p)
            if current_page >= cur_p:
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
                cur_p += 1
                if current_page >= cur_p:
                    cur_p += 1
                    if choice20 == choice20_options.get(0):
                        st.write("Sure, let's do something exceiting. How about something you've always wanted?")
                        st.write("Find Bolon for assistance and show him the following QR code (click next):\n")
                        if session_state.page_number >= cur_p:
                            img_path = make_qrcode(f"exciting mode",
                                save_path="./data/qrcode.png")
                            st.image(img_path)

                    elif choice20 == choice20_options.get(1):
                        st.write("Sure, let's do something quirky. \n")
                        text = st.text_input(label="Do you have something you want to say to Bolon? Type it in here, the hit next:\n")
                        if session_state.page_number >= cur_p:
                            st.markdown("""Show the following QR code to Bolon and he'll know what to do.
                            \(Of course, don't show him the message, or else, what's the fun?\)""")
                            img_path = make_qrcode(f"quirky mode: \n____message____\n{text}",
                                save_path="./data/qrcode.png")
                            st.image(img_path)

                    elif choice20 == choice20_options.get(2):
                        session_state.page_number = 0

        elif choice1 == choice1_options.get(1):
            cur_p += 1
            st.markdown(f"""You selected {choice1_options[1]}. 
            Sure, let's have some fun first. Click next for some funny videos:""")
            if cur_p <= session_state.page_number < cur_p + len(video_urls) - 1:
                url = video_urls[session_state.page_number -2]
                components.html(f"""
                <video width="320" height="240" controls>
                    <source src="{url}" type="video/mp4">
                </video>
                """,
                width=300, height=500)
                st.text("Click Next for more")
                print("moved to", session_state.page_number)
            elif session_state.page_number - cur_p>= len(video_urls) - 1:
                choice21_options = {
                    0: "That's it? You suck!",
                    1: "Let me go back!",
                }
                
                choice21 = st.radio(label="What do you do now?",
                    options=list(choice21_options.values()),
                    index=1)
                st.text("Going back")
                session_state.page_number = 0
            
        elif choice1 == choice1_options.get(2):
            cur_p += 1
            st.markdown(f"""You selected {choice1_options[2]}. 
            Sure, let's go down memory lane before officially turning 30. Click next please.""")
            
            if current_page >= cur_p:
                choice22 = st.date_input(label="How far back do you want to go?",
                    value=dt.date(2015, 3, 11),
                    min_value=dt.date(1992, 7, 31),
                    max_value=TODAY,
                    )
                cur_p += 1
                if session_state.page_number >= cur_p:
                    st.write(f"Ok! Let's go back from {choice22.strftime('%Y-%m-%d')}. Here you go...")
                    images = images_df.query("filedate>=@choice22")
                    
                    i = session_state.page_number - cur_p
                    # print(i)
                    if i in range(len(images)):
                        row = images.iloc[i]
                        st.text(f"{row.filedate.strftime('%B %d, %Y')}")
                        url = row.url
                        components.html(f"""{row.filename}
                        <img src="{url}" width="500" height="400" style="vertical-align:bottom">""",
                        width=800, height=600,
                        )
                        st.caption(
                                ":loudspeaker: Hint from JJ :dog: : Hit next to see what's next! Woof Woof!!"
                                )
                    else:
                        st.text(ending_text)
        
        elif choice1 == choice1_options.get(3):
            st.markdown("Ok! Got to [this link]('https://github.com/pauljhp/bolon/blob/master/data/boloncoupon.md') for you Bolon coupons")
        else: raise NotImplementedError
