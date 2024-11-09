# Apple Financial Data Chatbot

This chatbot provides answers and insights based on Apple Inc.’s financial data from 2020 to 2023. Built on the [Chainlit](https://www.chainlit.io/) framework, the bot utilizes natural language processing (NLP) to interpret user questions and return responses grounded in Apple’s financial reports.

## Features

- **Data-driven Insights**: Query Apple’s financial data directly to retrieve revenue, expenses, profit margins, and more for the years 2020 to 2023.
- **Natural Language Understanding**: The chatbot interprets and answers questions in natural language, making it accessible for users without a finance or technical background.
- **Trend Analysis**: Gain insights on year-over-year changes in revenue, profit, and other financial metrics.
- **User-Friendly**: Designed to engage and inform users with financial insights in an interactive way.

## Dataset

The chatbot is trained on Apple’s financial reports from the following years:
- **2020**: Annual report detailing revenue, expenses, and other financial metrics.
- **2021**: Updated report with insights on Apple's yearly performance.
- **2022**: Yearly data capturing trends and financial changes.
- **2023**: The most recent data available, providing a snapshot of Apple's latest financial performance.

These reports were parsed to extract relevant data points and metrics, including revenue growth, operating expenses, liabilities, and other key financial indicators.

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Chainlit](https://www.chainlit.io/) installed (`pip install chainlit`)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/phankhanhnghi/Chatbot_vgu.git
   cd Chatbot_vgu
   pip install -r requirements.txt
   chainlit run app.py -w
## Usage

1. Launch the application. A local URL will appear in the terminal (e.g., `http://localhost:8000`).
2. Open the URL in your browser to interact with the chatbot.
3. Ask questions related to Apple’s financial data, such as:
   - "What was Apple’s revenue in 2022?"
   - "How has Apple’s profit margin changed over the years?"
   - "What are Apple's major expenses for 2021?"

The chatbot will respond with relevant information based on the dataset.

## Examples of Questions

Here are some example queries to test with the chatbot:

- **Revenue**: "What was Apple’s total revenue in 2023?"
- **Profit Margin**: "How did Apple’s profit margin change from 2020 to 2023?"
- **Debt Analysis**: "What are Apple’s total liabilities in 2022?"
- **Operating Expenses**: "What were Apple’s operating expenses in 2021?"

## Project Structure

- `app.py`: Main application file for running the Chainlit chatbot.
- `data/`: Contains preprocessed financial data files for 2020-2023.
- `README.md`: Project documentation.
- `requirements.txt`: Python dependencies.

## Future Improvements

- **Expanded Dataset**: Adding more years of financial data to broaden the chatbot’s knowledge.
- **Enhanced NLP**: Improving the bot’s ability to understand complex, multi-part questions.
- **Data Visualization**: Integrating visual graphs to display trends in Apple’s financial performance over time.

## Acknowledgments

Special thanks to the Chainlit framework for providing an easy-to-use interface for chatbot development.

