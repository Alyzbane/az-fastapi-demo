def preprocess(text: str) -> str:
    """Preprocesses the input text by removing unwanted characters and normalizing it.

    Args:
        text (str): The input text to preprocess.

    Returns: 
        str: The preprocessed text.
    """

    new_text = []

    for t in text.split():
        # Remove URLs
        t = "@user" if t.startswith("@") and len(t) > 1 else t
        t = "http" if t.startswith("http") else t
        new_text.append(t)

    return " ".join(new_text)