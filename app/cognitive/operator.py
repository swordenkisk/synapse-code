import os
from openai import OpenAI
from app.schemas.blueprint import FinalCode
from app.prompts.system_prompts import OPERATOR_SYSTEM_PROMPT

class SynapseOperator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("MODEL_NAME", "gpt-4o")

    def generate_code(self, grid_blueprint: str):
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": OPERATOR_SYSTEM_PROMPT},
                {"role": "user", "content": f"Convert this Grid Blueprint to code:\n{grid_blueprint}"},
            ],
            response_format=FinalCode,
        )
        return response.choices[0].message.parsed
