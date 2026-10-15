from GROQ1 import generate_response
import time

def temperature_prompt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
    print("="*70)

    print("\nPART 1: TEMPERATURE EXPLORATION")
    base = input("Enter a creative prompt: ").strip()

    for t , label in (0.1, "LOW (0.1) - Deterministic"), (0.5, "MEDIUM (0.5) - Balanced"), (1.0, "HIGH (1.0) - Creative"):
        print(f"\n--- Temperature: {label} ---")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)

    print("\nPART 2: INSTRUCTION-BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, space exploration, AI ethics): ").strip()
    prompts = [
        f"Write a detailed essay on {topic}.",
        f"Summarize the key points about {topic} in a concise manner.",
        f"Provide a list of pros and cons regarding {topic}.",
        f"Explain {topic} in simple terms for a 10-year-old.",
        f"Create a fictional story that revolves around the theme of {topic}.",
    ]
    for i, p in enumerate(prompts, start=1):
        print(f"\n--- Instruction {i}: {p} ---")
        print(generate_response(p, temperature=0.7, max_tokens=512))
        time.sleep(1)

    print("\nPART 3: YOUR OWN INSTRUCTION PROMPT")
    custom = input("Enter your instruction-based prompt: ").strip
    try:
        temp = float(input("Enter a temperature value (0.0 to 1.0): ").strip())
    except ValueError:
        print("Invalid temperature value. Using default 0.7.")
        temp = 0.7

    print(f"\n--- Custom Instruction Prompt: {custom} ---")
    print(generate_response(custom, temperature=temp, max_tokens=512))

    print("\n--- Reflection ---")
    print("1) What changed when prompts became more specific?")
    print("2) What improved when context was added?")
    print("3) Which prompt yielded the most useful or relevant response from the AI? Why?")
    print("\nCHALLENGE: Create a prompt chain: ")
    print("Generate content -> rewrite it with constraints -> summarize it -> create a sequel (try different temperatures).")

def pseudo_stream(text, delayed = 0.013):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delayed)
    print()

def bonus_stream():
    choice = input("\nBONUS: streaming-like output? (y/n): ").lower().strip()
    if choice == "y":
        p = input("Enter a prompt: ").strip()
        out = generate_response(p, temperature=0.7, max_tokens=512)
        print("\nStreaming-like response (not real streaming):")
        pseudo_stream(out)

if __name__ == "__main__":
    temperature_prompt_activity()
    bonus_stream()
