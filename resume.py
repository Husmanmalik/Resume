import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
# image
Image1=Image.open('profile.png')
resized_img = Image1.resize((200, 200))
st.sidebar.image(resized_img)
# contact number
st.sidebar.title('Contact')
st.sidebar.text('Number: +923224750519')
st.sidebar.text('usmanmalik.citt@gmail.com')
col1, col2,col3 = st.sidebar.columns(3)
# linkedin
Image1=Image.open('linkedin.jpg')
resized_img = Image1.resize((50, 50))
resized_img.save('linkedin_s.jpg')
image_path = 'linkedin_s.jpg'
linkedin_link = 'https://www.linkedin.com/in/usman789'
col1.image(image_path)
col1.write(f"[LinkedIn Profile]({linkedin_link})")
# Github
Image1=Image.open('GitHub.png')
resized_img = Image1.resize((50, 50))
resized_img.save('github_s.png')
image_path = 'github_s.png'
github_link = 'https://github.com/Husmanmalik'
col2.image(image_path)
col2.write(f"[GitHub Profile]({github_link})")
#streamlit
Image1=Image.open('streamlit.jpg')
resized_img = Image1.resize((50, 50))
resized_img.save('streamlit_s.png')
image_path = 'streamlit_s.png'
streamlit_link = 'https://share.streamlit.io/signup'
col3.image(image_path)
col3.write(f"[Streamlit]({streamlit_link})")
st.title('Professional Experience:')
# Jeevaysoft
jeevaysoft="1-Jeevaysoft&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|5April2023-30December2023|"
st.subheader(jeevaysoft)
st.markdown('''
             US product base Company which facilitate lab in US.\n
             Tech support and Data Analysis: Addressing tech support ticket. Data sorting for Dashboard and Present it in visualization manner.\n
            • Collaborator: Coordinating with customers. Resolving 3 technical support tickets in a day.\n
            • Spokesman: Handling the chat box on Company website. Answering Query on Company website with help of Tawk.to tool.\n
            • Sorting: Data sorting and using that data into the dashboard and empowering client to deal their patient on web portal with help dashboard.\n
            • Formation: Using sorted data into sales and team dashboard. Driving new strategy for company client.\n           
''')
# Netkom
st.subheader('2-Netkom&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|16Feb2022-31Mar2022|')
st.markdown('''
            Vendor Company of Multinational Tech giant HUAWEI.\n
            System Engineer: Responsible for system installation on new data Center of PTCL and Jazz.\n
            • Coordinator: Communicator Between customer and 3-person team on side.\n
            • Facilitator: Collaborated with the customers and the team members to use the available resources to satisfy customer needs and deliver the results in 3 days.\n
            • Tester: After installing the system on the side have done the process of testing simultaneously. So, if any error occurs, we can tackle it at first .so it save our time plus it’s also reduced 10% company travel expenditure.\n
''')
# skills 
st.title("Skills")
data={'Skills':['Markdown','Data_visualization','Data_Wrangling','Data_Normalization','Satistical_Analysis','Mechine_Learning','Deep_Learning','MiniConda_Enviorment_Handling','Dashboard_Desiging','SQL'],
      'Rating':[4,4,4,4,3,4,3,4,4,3]}
df=pd.DataFrame(data)
fig=px.bar(data_frame=df,x='Skills',y='Rating',color='Skills')
st.plotly_chart(fig,use_container_width=True)

# Education
st.title('Education')
st.header('COMSATS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Lahore,Pakistan|') 
st.subheader('BS Electrical Engineering&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|September2017-August2023|') 
st.header('ISLAMIYA COLLEGE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |Lahore,Pakistan|')
st.subheader("F.Sc Pre-Engineering&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|March2014-March2016|")
# Professional Development
st.title("Professional Development:")
st.header("AMAL ACADEMY&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|March2023-June2023|")
st.markdown('''
            Initiative taken by Stanford University Alumni to induct professional, corporation skills in students.\n
            Mega Project in Amal: Empowering Student Finances.\n
            Work as a most valuable team player.\n
               • In the group of nine dedicated individuals. Our project focused on empowering students in terms of their finances. We established connections with international clients and secured orders, which we then assigned to students who possessed the required skills in fields such as engineering and graphic design. This initiative provided students with the opportunity to finance their studies and become less dependent on their parents. Throughout the project, we had the privilege of interacting with 50 different clients from various parts of the world. We ensured that the skillful students received 80% of the total earnings, while the remaining 20% was allocated for our team. The impact of our efforts was remarkable, as we witnessed numerous success stories and managed to bring about a 60% positive change in the lives of the students involved.\n
            Career-Prep Fellow:\n
               • Communication: Selected from 6000 applications for 3-month fellowship. This is funded by Stanford University. By completing a comprehensive written application and interview process.\n
               • Skills development: Investing 150-hours in this fellowship help me to polish my skills set Of (E.g. communication, leadership, problem solving, and teamwork.\n            
''')
#Academic Experirnce
st.title("Academic Experience:")
st.header("Seeding and spraying Robot for Agricultural Field\n\n|December 2020 – August 2021 |")
st.subheader("Innovative Project in the field of Agriculture\nProject leader: Circuit designer and installer with team of two persons.\n")
st.markdown('''
            <div style='text-align:left;'> 
            •  During final year project, in the team of three members demonstrated exceptional coordination and collaboration to develop a multitasking robot capable of both spraying and seeding operations.This innovative robot operates efficiently on a 12-volt battery, significantly reducing fuel consumption by 40%. Moreover, its integration with artificial intelligence enables the robot to scan the field and precisely identify areas infested with pests or insects. As a result, we were able to minimize the cost of spraying by 25%, as the robot selectively targets only the affected areas. This project not only enhances the ease of operations for farmers but also provides substantial financial relief, making a positive impact on their overall productivity and profitability.\n</div>
            ''',unsafe_allow_html=True)
#Project in powerBI and Python
st.title("Project in Power BI and SQL")
st.header("Sales Dashboard Formation")
st.markdown("""
            <div style='text-align:left;'> 
            Visual representation of sales based on their region and team in dashboard.\n
            Data Analyst: Showing Data into the productive manner and help the client to adopt new strategies according to the sorted data.\n
            • The newly formed dashboard provides a comprehensive overview of chocolate sales in seven regions across the world. Through the implementation of SQL query language, tables have been structured to capture relevant sales data. The dashboard seamlessly integrates power query and unpivoting techniques to present a visually appealing representation of the sales figures. Furthermore, the dashboard goes beyond mere numbers by incorporating images of the sales personnel who have contributed to achieving these sales milestones. This dynamic dashboard even includes a forecasting feature, enabling users to anticipate trends for the upcoming quarter. With its empowering capabilities, the dashboard offers a bird's-eye view of all the activities within the company, allowing users to monitor and analyze every aspect efficiently.\n
            </div>
""",unsafe_allow_html=True)
# Volunteer Experience
st.title("Extracurricular & Volunteer Experience")
st.header("IET CUI Lahore Society\n\n|September2017-August2021|")
st.markdown("""
             <div style='text-align:left;'>
             •	Event Manager: Organized the team of 5 person successfully.Invested time in advertisement of the Event, and with help of members able to increase 10% sales in Event tickets.\n
              </div>
""",unsafe_allow_html=True)
# online courses
st.title("Online Courses")
st.title("Awards and Honors")
st.markdown("""
            <div style='text-align:left;'>
            • Received merit-based Laptop Award from Chief Minister Punjab in (2018).\n
            • IET appreciation Award as best event organizer in (2018).\n
            </div>
""",unsafe_allow_html=True)
# Additional
st.title("Additional")
st.markdown("""
            <div style='text-align:left;'>
               • Technical Skills: Microsoft Office, Power BI , SQL ,Python.\n
               • Certifications: Microsoft Office (Organization or Institute, Year),Codanic(paython ka chilla).\n
               • Interests: Technology Management, News Stories.\n
               • Language: English, Urdu.\n
            </div>""",unsafe_allow_html=True)


