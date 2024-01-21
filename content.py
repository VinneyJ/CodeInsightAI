"""Description: This file contains the code to run the chatbot on the given repository."""
import os
from langchain.document_loaders import GitLoader
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain import PromptTemplate

def get_openai_api_key():
    """Get the OpenAI API key from the environment."""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    return api_key

def load_data_from_git(repo_url, local_path, branch_name):
    """Load the data from the Git repository."""
    loader = GitLoader(
        clone_url=repo_url,
        repo_path=local_path,
        branch=branch_name,
    )
    return loader.load()

def create_chroma_instance(data, embedding_function):
    """Create a Chroma instance from the given data."""

    return Chroma.from_documents(data, embedding_function)

def initialize_chatbot_chain(embedding_function, chain_type, search_k):
    """Initialize the chatbot chain."""

    db = create_chroma_instance(data, embedding_function)
    chatbot_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(
            temperature=0, model_name="gpt-3.5-turbo-16k", max_tokens=500
        ),
        chain_type=chain_type,
        retriever=db.as_retriever(search_kwargs={"k": search_k})
    )
    return chatbot_chain

def create_prompt_template():
    """Create a prompt template."""

    template = "respond as clearly as possible {query}?"
    return PromptTemplate(
        input_variables=["query"],
        template=template,
    )

def run_queries(chatbot_chain, prompt, queries):
    """Run the queries."""
    for query in queries:
        try:
            response = chatbot_chain.run(prompt.format(query=query))
            print(response)
        except Exception as e:
            print(f"An error occurred while processing query '{query}': {e}")

# Main execution
if __name__ == "__main__":
    openai_api_key = get_openai_api_key()
    
    # Load data from the Git repository
    data = load_data_from_git(
        repo_url="https://github.com/VinneyJ/penHouse",
        local_path="./penHouse",
        branch_name="main"
    )
    
    # Initialize the Chroma instance with the loaded data
    embedding_function = OpenAIEmbeddings()
    chatbot_chain = initialize_chatbot_chain(embedding_function, "valid_chain_type", 12)
    
    # Create a prompt template
    prompt_template = create_prompt_template()
    
    # Define queries to run
    queries = [
        "can you explain what is happening in this code base in 200 words?",
        "how many operations are available?",
        "can you suggest what code changes I need to do add a delete operation which deletes a specific post?",
        "can you generate a data flow diagram for the code base using mermaid syntax?"
    ]
    
    # Run the queries
    run_queries(chatbot_chain, prompt_template, queries)
