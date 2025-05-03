from serper_search import search_serper

query = "What is quantum computing?"
results = search_serper(query)

print("\n🔍 Serper Search Results:\n")
for i, r in enumerate(results, 1):
    print(f"{i}. {r}")
