import json
from langchain.callbacks.base import BaseCallbackHandler


class DiskRecordHandler(BaseCallbackHandler):
    def __init__(self):
        self.prompt = None
        self.response = None

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        # Storing the prompt to the instance variable
        self.prompt = prompts

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        # Storing the response to the instance variable
        self.response = response

        # Now that we have both prompt and response, we can write it to the disk
        with open('llm_records.json', 'a') as f:
            json.dump({"prompt": self.prompt, "response": self.response}, f)
            f.write("\n")
