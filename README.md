# FAQ BOT

This is an end to end LLM project based on Google Palm and Langchain. 

# Project Highlights

- Using a real CSV file of FAQs that Codebasics company is using right now. Their human staff will use this file to assist their course learners.
- This bot is not limited only to FAQs related to Codebasics you can confirm the format of csv file and can use you own CSV file to create you own FAQ bot.
- Building an LLM based question and answer system that can reduce the workload of their human staff.
- User will be able to use this system to ask questions directly and get answers within seconds

# Tech Stack Used 
- Langchain + Google Palm: LLM based Q&A
- Streamlit: UI 
- Huggingface instructor embeddings: Text embeddings
- FAISS: Vector databse

# Installation

1. Clone this repository to your local machine using:

    ```
    https://github.com/varayush007/Codebasics-Q-A.git
    ```

2. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Acquire an api key through makersuite.google.com and put it in .env file

    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```

# Usage 

1. Run the Streamlit app by executing:

    ```
    streamlit run main.py
    ```

2. The web app will open in your browser.

- To create a knowledebase of FAQs, click on Create Knolwedge Base button. It will take some time before knowledgebase is created so please wait.

- Once knowledge base is created you will see a directory called faiss_index in your current folder

- Now you are ready to ask questions. Type your question in Question box and hit Enter

# Sample Questions

- Do you guys provide internship and also do you offer EMI payments?

- Do you have javascript course?

- Should I learn power bi or tableau? 

- I've a MAC computer. Can I use powerbi on it?

- I don't see power pivot. how can I enable it?

# Project Structure

- main.py: The main Streamlit application script.

- langchain_helper.py: This has all the langchain code

- requirements.txt: A list of required Python packages for the project.

- .env: Configuration file for storing your Google API key.
