# CodeInsightAI

CodeInsightAI is a chatbot application that leverages the power of OpenAI's language models to provide answers to queries based on a given codebase. It uses a combination of document retrieval and language model querying to generate responses.

## Features

- Git repository integration for loading codebase data.
- Chroma vector store for efficient document retrieval.
- OpenAI language model embeddings for understanding and generating text.
- RetrievalQA chatbot chain for answering queries related to the codebase.
- Prompt templating for consistent query formatting.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Access to OpenAI API and an API key

### Installation

Clone the repository to your local machine:

```pip install requirements.txt```

### Configuration

Set the `OPENAI_API_KEY` environment variable with your OpenAI API key:

```export OPENAI_API_KEY='your-api-key-here'```

### Usage

To run the chatbot application, execute the following command:


The application will load the data from the specified Git repository, initialize the chatbot chain, and start processing the predefined queries.

## Development

To contribute to CodeInsightAI, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <PROJECT_NAME>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).


## Contact

If you want to contact me, you can reach me at vince1otieno@gmail.com.

## License

This project uses the following license: [MIT License]().