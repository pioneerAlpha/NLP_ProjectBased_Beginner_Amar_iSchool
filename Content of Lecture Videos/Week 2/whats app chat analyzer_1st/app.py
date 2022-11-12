import streamlit as st
import whatsapp_chat_analyzer, helper
import matplotlib.pyplot as plt

st.sidebar.title("Whatsapp chat analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = whatsapp_chat_analyzer.preprocess(data)

    st.dataframe(df)

    #fetch unique users
    user_list = df['users'].unique().tolist()
    # user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show Analysis", user_list) 


    if st.sidebar.button("Show Analysis"):
        num_messages,words, num_media_messages, links = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col_1, col_2, col_3, col_4 = st.columns(4)

        with col_1:
            st.header("Total Messages")
            st.title(num_messages)
        with col_2:
            st.header("Total Words")
            st.title(words)

        with col_3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col_4:
            st.header("Links Shared")
            st.title(links)


    #finding the busiest user in the group
    if selected_user == 'Overall':
        st.title("Most busy users")
        x,new_df = helper.most_busy_users(df)
        fig, ax = plt.subplots()

        col_1,col_2 = st.columns(2)

        with col_1:
            ax.bar(x.index, x.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col_2:
            st.dataframe(new_df)

