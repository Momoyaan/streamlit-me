import streamlit as st

with st.sidebar:
    st.markdown(
        """
        <ul style="list-style-type: none;">
                <li><a href="#introduction">Introduction</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#personal-life">Personal Life</a></li>
                <li><a href="#reflections">Reflections</a></li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

st.title("Autobiography")

st.subheader("Introduction")
st.markdown("""
My name is Ian Mathew M. Aviso and I was born on December 1, 2002 in Minglanilla, Cebu. I grew up in a loving family with my parents and older brother & sister. My father works as an electric engineer and my mother is a housewife.

I had a happy childhood, playing sports, riding bikes, and playing video games. I was a curious kid and loved learning about how things worked. Later on, I had great interest in Technology specfically Computers and decided I wanted to become a Software Engineer.
""")

st.subheader("Education")

st.markdown("""
I am currently attending college at Cebu Institute of Technology - University (CIT-U) and pursuing a degree in Information Technology. 

My studies focus on various aspects of Information Technology, including:
""")
st.markdown(
    """
    - Programming languages such as C/C++, Java, Python, and Javascript 
    - Data structures and algorithms
    - Networking
    - Database management systems
    - & More
    """
)
st.subheader("Personal Life")
st.write(
    "In my personal life, I have a strong interest in systems programming and operating systems. I am currently learning Rust, a systems programming language known for its performance, safety, and concurrency features. I am excited to explore the capabilities of Rust and apply it to low-level system development."
)
st.write(
    "Additionally, I have recently switched to using Linux as my daily driver operating system. By immersing myself in the Linux environment, I aim to gain a deeper understanding of the inner workings of operating systems and improve my command-line skills. I enjoy experimenting with different Linux distributions, configuring my development environment, and troubleshooting any issues that arise."
)
st.write("Outside of my technical pursuits, I also enjoy:")
st.markdown(
    """
    - Watching anime and movies
    - Reading manga and light novels
    - Listening to various music genres (I particularly love shoegaze & noise rock)
    """
)


st.subheader("Reflections")
st.write(
    "As I reflect on my journey so far, I am grateful for the opportunities and experiences that have shaped me personally."
)
st.write(
    "In my educational pursuits, I am excited to be learning and gaining a solid foundation in the field. The coursework and projects have challenged me to think critically and develop problem-solving skills that I know will be valuable in my future endeavors."
)
st.write(
    "On the personal front, my exploration of systems programming using Rust and my adoption of Linux as my daily driver have been incredibly rewarding. Diving into low-level programming and understanding the intricacies of operating systems have expanded my knowledge and skills in ways I never imagined. These experiences have ignited a passion for systems-level development and have motivated me to continue learning and pushing my boundaries."
)
st.write(
    "As I look ahead, I am eager to apply my knowledge and skills to real-world projects and make a positive impact in the field of technology. I am open to new opportunities and collaborations that will allow me to grow further and contribute to meaningful initiatives."
)
st.markdown("""
That's my story in a nutshell - an ordinary life but one I'm proud of and grateful for.
""")
