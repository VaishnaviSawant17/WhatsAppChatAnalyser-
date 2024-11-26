import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8") #UTF stands for UCS (Unicode) Transformation Format
    df = preprocessor.preprocess(data)  # create dataframe

    st.dataframe(df)  # to display dataframe

    # fetch unique users

    user_list = df['user'].unique().tolist()  # create user list from chats
    user_list.remove('notification')  # to remove notification which we create for no user
    user_list.sort()  # for sort users in ascending order
    user_list.insert(0, "Overall")  # for show all users in listbar

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)  # we store stats in variable

    if st.sidebar.button("Show Analysis"):  # add button for statistics button

        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,
                                                                                df)  # for helper we use selected user variable and dataframe #code for total messages
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)  # to display total messages
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Total Links Shared")
            st.title(num_links)

        #  MONTHLY TIMELINE
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #  DAILY TIMELINE
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='violet')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #  ACTIVITY MAP
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='pink')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # ACTIVITY HEATMAP
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        #  finding the busiest users in the group(Group level)

        if selected_user == "Overall":
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()  # figure , axis

            col1, col2 = st.columns(2)

            with col1:  # to create bar chart of busiest user
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:  # percentage of users contribution
                st.dataframe(new_df)

    # WordCloud
    st.title("WordCloud")
    df_wc = helper.create_wordcloud(selected_user, df)  # call from helper create image and store in df_wc
    fig, ax = plt.subplots()
    ax.imshow(df_wc)  # to display image we use matplotlib and pass variable fig and axis
    st.pyplot(fig)

    # most common words
    most_common_df = helper.most_common_words(selected_user, df)

    # st.write(most_common_df)
    # st.write(most_common_df.columns)

    fig, ax = plt.subplots()

    ax.barh(most_common_df['word'], most_common_df['count'])
    plt.xticks(rotation='vertical')

    st.title('Most common words')
    st.dataframe(most_common_df)
    st.pyplot(fig)

    #  EMOJI ANALYSIS

    emoji_df = helper.emoji_helper(selected_user, df)
    st.title("Emoji Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(emoji_df)
    with col2:
        fig, ax = plt.subplots()
        ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%.2f")  # decimal
        #  plt.bar(emoji_df[0].head(),emoji_df[1].head())
        st.pyplot(fig)