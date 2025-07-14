from pydantic import BaseModel

class TextClassificationInput(BaseModel):
    input_text_list: list[str]

class ResponseDict(BaseModel):
    output: dict[str, dict[str, float]]

    class Config:
        json_schema_extra = {
            "example": {
                "output": {
                    "Good food!": {
                        "negative": 0.01,
                        "neutral": 0.01,
                        "positive": 0.98,
                    },
                    "Awful food!": {
                        "negative": 0.96,
                        "neutral": 0.02,
                        "positive": 0.02,
                    }
                }
            }
        }
