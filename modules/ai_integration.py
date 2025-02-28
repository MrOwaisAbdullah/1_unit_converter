from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

def get_ai_conversions(conversion_type: str, unit_from: str, value: str, unit_to: str, realtime_rate: float = None) -> str:
    """
    Uses Gemini API for complete conversion (except currency which uses real-time rates)
    """
    if conversion_type == "Currency" and realtime_rate:
        prompt = (
            f"Convert {value} {unit_from} to {unit_to} using this real-time exchange rate: 1 {unit_from} = {realtime_rate} {unit_to}. "
            f"Respond STRICTLY in format: '[NUMERICAL_RESULT]|Explanation (Additional context)'\n"
            f"Example: '96.00|{value} {unit_from} × {realtime_rate} {unit_to}/{unit_from} = {value*realtime_rate} {unit_to}. "
            "Currency values fluctuate based on market conditions like interest rates and economic performance. (Rate current as of [date/time])'"
        )
    else:
        prompt = (
            f"Convert {value} {unit_from} to {unit_to} with detailed explanation. "
            "Respond in format: 'NUMERICAL_RESULT|Formula (Short historical context)'\n"
            "Example: '32.8084|[value] × 3.281 = [result] (1 foot = 0.3048m since 1959)'"
            "Example is only for refference and put the value and result in the placeholders"
        )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=150,
                temperature=0.3
            )
        )
        return response.text
    except Exception as e:
        return f"AI Conversion Error: {str(e)}"