
---

## 📁 Folder: `modules/`

### 📄 `grammar.py`

```python
import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def correct_grammar(sentence):
    prompt = f"Correct this sentence and explain the mistake simply for A1–A2 level:\n'{sentence}'"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
