from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

class SpeedTestResult(BaseModel):
    download: float | None
    ping: float | None
    upload: float | None

parser = JsonOutputParser(pydantic_object=SpeedTestResult)