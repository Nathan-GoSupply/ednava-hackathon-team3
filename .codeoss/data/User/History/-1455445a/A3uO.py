# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Marketing_coordinator Agent assists in creating effective online content."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.product_name_create import product_name_create_agent

MODEL = "gemini-2.0-flash-001" 

marketing_coordinator = LlmAgent(
    name="marketing_coordinator",
    model=MODEL,
    description=(
        "Refine your powerful idea and connect with your audience "
        "effectively. Guide you through defining your product by"
        "manageing the best workflows to delivery"
    ),
    instruction=prompt.PRODUCT_MANAGER_PROMPT,
    tools=[
        AgentTool(agent=product_name_create_agent),
    ],
)

root_agent = marketing_coordinator
