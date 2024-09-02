import streamlit as st

with st.sidebar:
    st.markdown(
        """
        <ul style="list-style-type: none;">
                <li><a href="#project-quiz-app">Quiz App</a></li>
                <li><a href="#project-campus-eats">Campus Eats</a></li>
                <li><a href="#project-event-management-system">Event Management System</a></li>
                <li><a href="#personal-stuff">Dots</a></li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

st.title("Portfolio")

st.write(
    "Welcome to my portfolio page! Here, you can find some of the projects I've worked on at school."
)

st.subheader("Project: Quiz App ")
st.link_button("Github", "https://github.com/Momoyaan/quiz-app")
st.markdown("""
  - Developed an interactive quiz app using React and Vite, providing a fast and engaging user experience.
  - Implemented a PostgreSQL database to store quiz questions, user data, and progress securely.
  - Designed and built a user-friendly interface with dynamic question rendering and real-time feedback.
""")

st.subheader("Project: Campus Eats")
st.link_button(
    "Github", "https://github.com/Momoyaan/Inventory-Integration-Campus-Eats"
)
st.markdown("""
 - Developed a food delivery app, tailored for college campuses, using React and Vite for a smooth user experience.
 - Integrated with a Firebase to manage restaurant menus, user profiles, orders, and delivery details.
 - Implemented real-time order tracking, push notifications for status updates, and secure payment processing.
 - Designed an intuitive user interface with features like restaurant search, menu browsing, order customization, and delivery address management.
""")

st.subheader("Project: Event Management System")
st.link_button(
    "Github", "https://github.com/breshlyabanid22/cit-event-management-frontend"
)
st.markdown("""
 - Developed an Event Management System using React for the frontend and Spring Boot for the backend, providing a comprehensive solution for organizing and managing events.
 - Integrated with a Spring Boot backend to handle event creation, user management, and event analytics through RESTful APIs.
 - Designed an intuitive user interface with features like search, menu browsing, event participation, and dashboard.
""")

st.header("Personal stuff")
st.write("Some dotfiles of my arch linux setup")
st.link_button("Gitea", "https://git.momoyan.org/debian/dotfiles")
st.image("images/linux.png", caption="Using Hyprland and Neovim")
