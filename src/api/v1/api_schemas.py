from pydantic import BaseModel, Field

class TextClassificationInput(BaseModel):
    input_text_list: list[str] = Field(
        ...,
        default_factory=list,
        description="List of input text strings to classify.",
        max_length=1000,
    )

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
