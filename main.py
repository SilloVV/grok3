from grok3_utils import call_grok

if __name__ == "__main__":
    query = input("Enter your query: ")
    
    print("Réponse: ", end="")
    generator = call_grok(query)
    
    try:
        for chunk in generator:
            print(chunk, end="", flush=True)
    except StopIteration as e:
        result = e.value
        print(f"\n\nTokens: {result['input_tokens']} input, {result['output_tokens']} output")