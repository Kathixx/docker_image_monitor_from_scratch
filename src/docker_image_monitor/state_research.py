
from pydantic import BaseModel, Field

# ===== STATE DEFINITIONS =====
# reusing the state definitions of the version agent

# ===== STRUCTURED OUTPUT SCHEMAS =====
class Summary(BaseModel):
    """Schema for webpage content summarization."""
    summary: str = Field(description="Concise summary of the webpage content")
    key_excerpts: str = Field(description="Important quotes and excerpts from the content")

class Findings(BaseModel):
    """Schema for webpage content summarization and evaluation."""
    name_version: str = Field(description="Docker image name and version")
    summary: str = Field(description="Concise summary of the webpage content")
    criticality: str = Field(description="Evaluation and scoring of the updates")
    recommandation: str = Field(description="Recommandation for the development team")

