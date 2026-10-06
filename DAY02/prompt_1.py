import ollama
while True:
    question =input("Ask questions:")
    if questions.lower() =="exit":
        break
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role" : "system",
            "content",: "Give answers in 2 lines only",
        },
    ]
)
  print(response["message"]["content"])