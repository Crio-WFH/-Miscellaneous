# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:36:33 2021

@author: admin
"""
#importing libraries
import streamlit as st
import pandas as pd
import base64
#importing functions from database file
from db_functions import create_table,add_data,view_all_data,view_all_task_names,get_task,edit_task_data,delete_data

hide_streamlit_style = """            
                       <style>            
                       #MainMenu {visibility: hidden;}            
                       footer {visibility: hidden;}            
                       </style>            
                       """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("To-Do App")
st.sidebar.title("Menu")

 #sidebar for navigation  
page = st.sidebar.radio(" ", ('Add','Update','Delete','Select Music'))
table = pd.DataFrame([])

if page == "Add":
    st.image('https://images.unsplash.com/photo-1496449903678-68ddcb189a24?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80',width = 700)
    st.subheader("Add a task")
    col1, col2 = st.beta_columns(2)
    with col1:
        Task = st.text_input("Task Name",key = "<uniquevalueofsomesort>")
        Task_type = st.selectbox("Task Status", ("To-Do","Doing","Done"))
    with col2:
        #st.markdown("###")
        due_date = st.date_input("Due on")
        due_time = st.time_input("Time")
    if st.button("Add Task"):
        create_table()
        add_data(Task,Task_type,due_date,due_time)
        st.success("Task Added")
        with st.beta_expander("View Task List"):
            list_of_tasks = view_all_data()
            df = pd.DataFrame(list_of_tasks,columns=["Task","Status","Date","Time"])
            st.dataframe(df)
        def get_table_download_link_csv(df):
            csv = df.to_csv().encode()
            b64 = base64.b64encode(csv).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="Tasks.csv" target="_blank">Download tasks csv file</a>'
            return href
        st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
        

elif page == "Update":
    st.subheader("Edit/Update Task List")
    task_list = [i[0] for i in view_all_task_names()]
    task_to_edit = st.selectbox("Select the Task to Edit",task_list)
    edit_task = get_task(task_to_edit)

    if edit_task:
            Task = edit_task[0][0]
            Task_type = edit_task[0][1]
            due_date = edit_task[0][2]
            due_time = edit_task[0][3]
            
            col1,col2 = st.beta_columns(2)
            			
            with col1:
                new_task = st.text_input("Edit Task Name",Task)
                new_task_type= st.selectbox("Edit Status",["To-Do","Doing","Done"])
               
            
            with col2:
                new_task_due_date = st.date_input("Edit Due Date")
                new_task_due_time = st.time_input("Edit Due Time")
                
            
            if st.button("Update Task"):
                edit_task_data(new_task,new_task_type,new_task_due_date,new_task_due_time,Task,Task_type,due_date,due_time)
                st.success("Task Updated")
            
            with st.beta_expander("View Updated Task List"):
                result = view_all_data()
                
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date","Time"])
                st.dataframe(clean_df)
    
elif page == "Delete":
    st.subheader("Delete a Task")
    task_list = [i[0] for i in view_all_task_names()]
    task_to_del = st.selectbox("Select the Task to Delete",task_list)
    if st.button("Delete Task"):
        del_task = delete_data(task_to_del)
        st.success("Task Deleted")
    with st.beta_expander("View Updated Task List"):
        result = view_all_data()
                
        clean_df = pd.DataFrame(result,columns=["Task","Status","Date","Time"])
        st.dataframe(clean_df)
    
    
    
elif page == "Select Music":
    st.image('https://images.unsplash.com/photo-1507120410856-1f35574c3b45?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80',width = 700)
    st.subheader("Select Soothing Music of Your Choice to Enjoy While Completing Your Tasks")
    with st.beta_expander("Nature Sounds"):
        st.video("https://www.youtube.com/watch?v=6oAdJjzXQS8", format='video/mp4')
        st.write("Copyright: Music: OCB Relax. Footage, photo licensed via shutterstock and 123rf from various artists. Copyright © 2021 OCB Relax. All rights reserved.")
    with st.beta_expander("Instrumental"):
        st.video("https://www.youtube.com/watch?v=ONLQeCWcxAY", format='video/mp4')
        st.write("Copyright: Tim Janis")
    with st.beta_expander("Ambient Sounds"):
        st.video("https://www.youtube.com/watch?v=OKHSQveDPMk", format='video/mp4')
        st.write("Copyright: Music - OCB Relax. Thumbnail picture licensed from pat138241 via 123rf.com. Copyright © 2021 OCB Relax. All rights reserved. Video reference number: 236")
    with st.beta_expander("Raining White Noise"):
        st.video("https://www.youtube.com/watch?v=9oc8Fa7tb8c", format='video/mp4')
        st.write("Copyright: © Relaxing White Noise LLC, 2019")
