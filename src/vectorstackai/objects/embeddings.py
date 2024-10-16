import requests
import base64
import numpy as np
class BaseObject:
    response: requests.Response = None

class EmbeddingsObject(BaseObject):
    """
    Object returned by the Embedding API

    Attributes:
        embeddings (List[List[float]]): The list of embeddings returned by the API
    """
    def __init__(self, response, dimension):
        self.response = response
        self.embeddings = None
        if response.status_code == 200:
            # Get the base64 encoded embeddings string
            embeddings_base64 = response.json()['output']['embeddings']
            
            # Decode the base64 string back into bytes
            embeddings_bytes = base64.b64decode(embeddings_base64)
            
            # Convert the byte string back into a NumPy array
            self.embeddings = np.frombuffer(embeddings_bytes, dtype=np.float32).reshape(-1, dimension)
        
    def __str__(self) -> str:
        if self.embeddings:
            num_embeddings = len(self.embeddings)
            embedding_dims = len(self.embeddings[0])
            return f"EmbeddingsObject(num_embeddings={num_embeddings}, embedding_dims={embedding_dims})"
        else:
            return "Error: EmbeddingsObject(no embeddings returned)"
        
    def __repr__(self) -> str:
        return self.__str__()   