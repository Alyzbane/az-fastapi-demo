import torch
from typing import Annotated
from scipy.special import softmax
from fastapi import APIRouter, Request, Depends, HTTPException, Body
from loguru import logger

from src.security import auth_api_key
from src.api.v1.api_schemas import TextClassificationInput, ResponseDict
from src.preprocess_helpers import preprocess  

router = APIRouter(
    prefix="/classification",
    dependencies=[Depends(auth_api_key)],
)

@router.get("/")
async def read_root(request: Request):
    return {"message": "Welcome to the Text Classification API!"}

@router.post("/score/", response_model=ResponseDict)
async def score(request: Request, input_data: Annotated[TextClassificationInput, Body()]):

    model = request.app.model
    labels = request.app.labels
    tokenizer = request.app.tokenizer

    if not model or not tokenizer or not labels:
        logger.error("Model, tokenizer, or labels not initialized in the app context.")
        raise HTTPException(status_code=500, detail="Model not initialized")    

    # Process user input strings - make required string subs and tokenize
    user_input_list = input_data.input_text_list
    processed_user_input_list = [preprocess(single_input_string) for single_input_string in user_input_list]
    encoded_input = tokenizer(processed_user_input_list, padding=True, return_tensors='pt')

    # Run through model and normalize
    with torch.no_grad():
        scores = model(**encoded_input)[0].detach().numpy()
    scores_normalized = softmax(scores, axis=1).tolist()

    # Bind to original data (input text after processing: scores)
    output_dict = {}
    for text, scores in zip(processed_user_input_list, scores_normalized):
        scores_dict = {k:v for k,v in zip(labels, scores)}
        output_dict[text] = scores_dict

    return {'output': output_dict}