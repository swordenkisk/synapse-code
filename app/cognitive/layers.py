import os
from openai import OpenAI
from app.schemas.blueprint import ArrayLayer, LatticeLayer, TensorLayer, GridLayer
from app.prompts.system_prompts import ARCHITECT_SYSTEM_PROMPT

class SynapseBrain:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("MODEL_NAME", "gpt-4o")

    def process_blueprint(self, user_goal: str):
        # 1. The Array
        array = self._run_layer(user_goal, ArrayLayer, "Decompose into linear requirements.")
        
        # 2. The Lattice
        lattice = self._run_layer(array.model_dump_json(), LatticeLayer, "Map dependencies.")
        
        # 3. The Tensor
        tensor = self._run_layer(lattice.model_dump_json(), TensorLayer, "Analyze multi-dimensional trade-offs.")
        
        # 4. The Grid
        grid = self._run_layer(tensor.model_dump_json(), GridLayer, "Create the final English blueprint.")
        
        return {"array": array, "lattice": lattice, "tensor": tensor, "grid": grid}

    def _run_layer(self, input_data: str, schema, instruction: str):
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": ARCHITECT_SYSTEM_PROMPT},
                {"role": "user", "content": f"{instruction}\nInput: {input_data}"},
            ],
            response_format=schema,
        )
        return response.choices[0].message.parsed
