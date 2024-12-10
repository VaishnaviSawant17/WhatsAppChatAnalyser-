
# WhatsApp Chat Analyzer

A Streamlit app to analyze and visualize WhatsApp chat data. This app helps users to gain insights into their chat history, including statistics on messages, words, media shared, emojis used, and more.

## Features

- **File Upload**: Upload a WhatsApp chat file (.txt format).
- **User-specific Analysis**: View statistics and visualizations for a specific user or the entire group.
- **Top Statistics**: Total messages, words, media shared, and links.
- **Timelines**: Monthly and daily message timelines.
- **Activity Maps**: Visualize the most active days and months.
- **Heatmaps**: Analyze user activity patterns throughout the week.
- **WordCloud**: Visualize the most frequent words used in the chat.
- **Most Common Words**: Bar chart of the most common words used in the conversation.
- **Emoji Analysis**: Analyze and visualize the most frequently used emojis.

## How to Use

1. **Upload your WhatsApp Chat**:
   - Prepare your WhatsApp chat data in `.txt` format.
   - Click on the "Choose a file" button in the sidebar to upload the file.

2. **Select a User**:
   - Choose a specific user or "Overall" to analyze the entire group's activity.
   
3. **Click on 'Show Analysis'**:
   - The app will display various statistics and visualizations such as:
     - Total messages, words, media, and links shared.
     - Monthly and daily timelines.
     - Activity heatmaps, most busy users, and emoji usage.

## Technologies Used

- **Streamlit**: To build the interactive web app.
- **Python**: For backend processing and data manipulation.
- **Pandas**: For handling and processing chat data.
- **Matplotlib & Seaborn**: For creating plots and visualizations.
- **WordCloud**: For generating the word cloud from chat data.

## Installation

### Prerequisites

- Python 3.x
- Install the required libraries using `pip`:

```bash
pip install streamlit pandas matplotlib seaborn wordcloud
