
# Article Generator Chatbot with LLMs

## Overview
This repository contains the implementation of an article generator chatbot that leverages three open-source large language models (LLMs): GPT-2, BLOOM, and GPT-Neo. The chatbot is designed to generate articles on various topics based on user input. It evaluates and compares the performance of these models in terms of speed and article quality.

## Task 1: Article Generator Chatbot

### Description
The goal of this task is to build a chatbot that can generate articles based on a given topic using three different LLMs. The models used for the task are:
1. GPT-2 (`gpt2`)
2. BLOOM (`bigscience/bloom-560m`)
3. GPT-Neo (`EleutherAI/gpt-neo-1.3B`)

The task includes evaluating the performance of these models, identifying the best model for article creation, and providing a report based on the evaluations.

### Requirements
- Python 3.7 or higher
- The following Python packages are required:
  - `transformers`
  - `torch`
  - `sys`

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Model Weights
The models are available through the Hugging Face `transformers` library. Ensure that you have internet access to download the models the first time you run the chatbot.

If the model weights are large, consider uploading them to a cloud storage service (e.g., Google Drive) and provide the download link in the `README.md` if needed.

### How to Run
To run the chatbot:

1. Clone the repository:

```bash
git clone https://github.com/Tithibanerjee29/NULLCLASS_INTERNSHIP.git
cd NULLCLASS_INTERNSHIP
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the `chatbot.py` script:

```bash
python chatbot.py
```

4. Follow the on-screen instructions to enter a topic and select a model for generating the article.

### Models Evaluation
The models are evaluated based on the time taken to generate the article and the quality of the generated text. The performance results of each model are stored in a report file (`comparison_report.txt`).

### Comparison Report
The comparison report is generated after running the chatbot. It includes the following metrics for each model:
- Time taken to generate the article
- A snippet of the generated article (first 300 characters)

The report can be found in the `comparison_report.txt` file.

### Code Overview
- `chatbot.py`: Main script that runs the chatbot and interacts with the user.
- `comparison_report.txt`: Contains the evaluation results for each model.
- `requirements.txt`: Lists the required dependencies for the project.

### Submission Guidelines
1. Ensure all tasks are organized into separate folders.
2. Include a `requirements.txt` file with all dependencies.
3. Provide saved models if necessary (upload to Google Drive and include the link in the `README.md`).
4. Submit the code, models, and the report via GitHub.
5. Ensure that the task is integrated within the framework of the course curriculum, not treated as a separate task.


