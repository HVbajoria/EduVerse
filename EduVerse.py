import json
from pathlib import Path

# Setup
import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
from auth0_component import login_button

domain = "dev-qzlbx0jqzsgjkeaf.us.auth0.com"
clientId = "MxxNJ7qlS1CLzusDdY10wIjYYStaswk4"
auth0_client_secret = "AhmJasxlnHfhl2Eop4krFvO_JEW9OTmuD7twFoU6xpX6ZBbMsKnUDMziuc4ZGRg2"


DEFAULT_PAGE = "EduVerse.py"
SECOND_PAGE_NAME = "welcome"

st.set_page_config( 
     page_title="EduVerse", 
     page_icon="🏫", 
 ) 

def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break


clear_all_but_first_page()



# Password and email fetch
def login_user(email, password):
    return "hi"



if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# Main function
def main():
    # """Login page"""
    
    hide_default_format = """ 
        <style> 
        #MainMenu {visibility: show; } 
        footer {visibility: hidden;} 
        </style> 
        """ 
    st.markdown(hide_default_format, unsafe_allow_html=True) 

    def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

    color1 = "#0d3270"
    color2 = "#0fab7b"
    text = "EduVerse"
  
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("images/logo.png", width=200)

    styled_text = gradient_text(text, color1, color2)
    st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)
    st.title("Welcome to EduVerse!")
    menu = ["Login", "SignUp"]
    choice = st.selectbox(
        "Select Login or SignUp from dropdown box ▾",
        menu,
    )
    st.markdown(
        "<h10 style='text-align: left; color: #ffffff;'> If you do not have an account, create an accouunt by select SignUp option from above dropdown box.</h10>",
        unsafe_allow_html=True,
    )
    if choice == "":
        st.subheader("Login")
    elif choice == "Login":
        st.write("-------")
        st.subheader("Log in to the App")

        user_info=login_button(clientId, domain = domain)
        st.write(user_info)
            # # if password == '12345':
            # # Hash password creation and store in a table

            # result = login_user(email,password)
            # if result:
            #     st.session_state["logged_in"] = True

            #     st.success("Logged In as {}".format(email))

            #     if st.success:
            #         st.subheader("User Profiles")
                   
            # else:
            #     st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.write("-----")
        st.subheader("Create New Account")
        new_user = st.text_input("Username", placeholder="name")
        new_user_email = st.text_input("Email id", placeholder="email")
        new_password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if new_user == "":  # if user name empty then show the warnings
                st.warning("Inavlid user name")
            elif new_user_email == "":  # if email empty then show the warnings
                st.warning("Invalid email id")
            elif new_password == "":  # if password empty then show the warnings
                st.warning("Invalid password")
            else:
                st.success("You have successfully created a valid Account")
                st.info("Go up and Login to you account")

    if st.session_state["logged_in"]:
        show_all_pages()
        hide_page(DEFAULT_PAGE.replace(".py", ""))
        switch_page('welcome')
    else:
        clear_all_but_first_page()

if __name__ == "__main__":
    main()