import sys
import json
import subprocess

raw_input = sys.stdin.read().strip()

if not raw_input:
    print("No input received.")
    sys.exit(0)

data = json.loads(raw_input)
text = data.get("text", "")

if "symptom" in text.lower():
    prompt = (
        "You are a medical specialist. "
        "Identify the symptom(s) and suggest a possible diagnosis. "
        "Three lines maximum.\n\n"
        f"Text:\n{text}"
    )

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Erro ao chamar o ollama:")
        print(result.stderr.strip())
    else:
        print(result.stdout.strip())
else:
    print("No clinical suggestion.")
#Get-Content test_with_symptoms.json | python chamallm.py