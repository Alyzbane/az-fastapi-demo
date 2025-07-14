from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

from loguru import logger

def download_model(model_name: str) -> tuple:
    """
    Downloads the specified model and tokenizer from Hugging Face.

    Args:
        model_name (str): The name of the model to download.

    Returns:
        tuple: A tuple containing the tokenizer and the model.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

if __name__ == "__main__":
    task = "sentiment"
    model_name = f"cardiffnlp/twitter-roberta-base-{task}"
    tokenizer, model = download_model(model_name)

    logger.info(f"Downloaded model: {model_name}")