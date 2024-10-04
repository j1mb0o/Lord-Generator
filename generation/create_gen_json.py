import json

# Read the generated poems
with open("byron_generated_poems.json", "r") as f:
    generated_poems = json.load(f)

# Create a list to hold the new poem objects
structured_poems = []

# Process each poem
for poem in generated_poems:
    lines = poem.split('\n')
    poem_object = {
        "title": "",  # Title can be set if known
        "author": "Generated",
        "lines": "\n".join(lines),
        "linecount": str(len(lines))
    }
    structured_poems.append(poem_object)

# Write the new structured poems to a new JSON file
with open("structured_byron_generated_poems.json", "w") as f:
    json.dump(structured_poems, f, indent=2)