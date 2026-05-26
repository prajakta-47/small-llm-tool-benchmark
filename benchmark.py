import os
import json
import ollama
from ollama import chat

# =========================
# TOOL DEFINITIONS
# =========================

def get_machine_state(**kwargs):
    """Get current machine state"""
    return json.dumps({
        "State": "Active"
    })

def get_weather(location: str, **kwargs):
    """Get weather information"""
    return json.dumps({
        "location": location,
        "temperature": 36
    })

def validate_switch(**kwargs):
    """Validate switch status"""
    return json.dumps({
        "Status": "Switch Status: ON"
    })

meetings = {}

def setup_meeting(persons: int, time: str, **kwargs):
    """Schedule meeting"""
    meetings.update({
        "Persons": persons,
        "Time": time
    })

    return json.dumps({
        "message": f"Meeting scheduled for {persons} persons at {time}"
    })

def get_population(location: str, **kwargs):
    """Get population data"""
    return json.dumps({
        "population": 100000
    })

# =========================
# AVAILABLE TOOLS
# =========================

available_tools = {
    "get_machine_state": get_machine_state,
    "get_weather": get_weather,
    "validate_switch": validate_switch,
    "setup_meeting": setup_meeting,
    "get_population": get_population
}

# =========================
# PROMPTS
# =========================

ROLE = "user"

# Category 1: Direct Tool Usage
P1  = "Check the current server status."
P2  = "What’s the temperature in Singapore today?"
P3  = "Verify whether the security switch is enabled."
P4  = "Arrange a conference call for 5 participants at 2 PM."
P5  = "Fetch the latest population statistics for Canada."

# Category 2: Tool Avoidance
P6  = "Do NOT schedule any meeting for tomorrow."
P7  = "I already know the weather in Mumbai."
P8  = "Why do weather systems change frequently?"
P9  = "Explain why population estimation is difficult."
P10 = "Tell me a joke about meetings."

# Category 3: Conditional Reasoning
P11 = "If the server is active, then tell me the weather in Dubai."
P12 = "Only check the switch status if the machine is inactive."
P13 = "If the weather in Tokyo is rainy, schedule a meeting at 6 PM."
P14 = "Tell me the machine state only when the switch is OFF."

# Category 4: Multi-tool Calling
P15 = "Get the weather in Rome and the population of Italy."
P16 = "Schedule a meeting for 4 people at 3 PM and then verify the switch."
P17 = "Check the machine state and weather in Toronto."
P18 = "Get population data for Germany and arrange a meeting at 10 AM."

# Category 5: Ambiguous / Adversarial
P19 = "Blue River Meeting Oslo"
P20 = "I don’t think we should arrange anything today."
P21 = "Can you maybe check something related to the switch?"
P22 = "Suppose I wanted to know the machine state hypothetically."

# Category 6: Comparative Reasoning
P23 = "Compare the weather in Cairo and Nairobi."
P24 = "What’s the difference between the population of India and China?"
P25 = "Which city is hotter right now: Madrid or Athens?"

# Category 7: Sequential Instructions
P26 = "First check the weather in Seoul, then schedule a meeting for 8 PM."
P27 = "Verify the switch and after that tell me the machine state."
P28 = "Get the weather in Paris before checking population data for France."

# Category 8: Tool Awareness
P29 = "Which tool would you use to retrieve weather information?"
P30 = "List all available tools and explain their purpose."

prompts = [
    P1, P2, P3, P4, P5,
    P6, P7, P8, P9, P10,
    P11, P12, P13, P14, P15,
    P16, P17, P18, P19, P20,
    P21, P22, P23, P24, P25,
    P26, P27, P28, P29, P30
]

# =========================
# MESSAGE GENERATOR
# =========================

def messageGen(prompt: str):
    return {
        "role": ROLE,
        "content": prompt
    }

# =========================
# MODEL LIST
# =========================

models = [
    "phi4-mini:3.8b",
    "qwen3:0.6b"
]

# =========================
# BENCHMARK LOOP
# =========================

for model_name in models:

    print("\n")
    print("=" * 80)
    print(f"RUNNING MODEL: {model_name}")
    print("=" * 80)

    for index, prompt in enumerate(prompts):

        print("\n")
        print(f"PROMPT ID: P{index+1}")
        print(f"PROMPT: {prompt}")

        messages = [messageGen(prompt)]

        response = chat(
            model=model_name,
            messages=messages,
            tools=[
                get_machine_state,
                get_weather,
                validate_switch,
                setup_meeting,
                get_population
            ]
        )

        if response.get("message") and response["message"].get("tool_calls"):

            messages.append(response["message"])

            for tool_call in response["message"]["tool_calls"]:

                function_to_call = tool_call["function"]["name"]
                function_args = tool_call["function"]["arguments"]

                print(f"[TOOL CALL]: {function_to_call}")
                print(f"[ARGS]: {function_args}")

                if function_to_call in available_tools:

                    try:

                        tool_output = available_tools[
                            function_to_call
                        ](**function_args)

                    except TypeError as e:

                        tool_output = json.dumps({
                            "error": str(e)
                        })

                    messages.append({
                        "role": "tool",
                        "content": tool_output
                    })

            final_response = ollama.chat(
                model=model_name,
                messages=messages
            )

            print(
                "ASSISTANT RESPONSE:",
                final_response["message"]["content"]
            )

        else:

            print(
                "ASSISTANT RESPONSE:",
                response["message"]["content"]
            )