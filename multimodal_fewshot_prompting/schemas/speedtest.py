from pydantic import BaseModel, Field
from typing import Optional

class SpeedTestResult(BaseModel):
    download: Optional[float] = Field(
        default=None, 
        description="Download speed in Mbps"
    )
    ping: Optional[float] = Field(
        default=None, 
        description="Ping in ms"
    )
    upload: Optional[float] = Field(
        default=None,
        description="Upload speed in Mbps"
    )