items = input().split()

freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Purchase frequency:")
for item, count in freq.items():
    print(f"{item}: {count}")

most_popular = max(freq, key=freq.get)
print("\nMost popular item:", most_popular)

once = [item for item, count in freq.items() if count == 1]
print("\nPurchased once:", " ".join(once))

sorted_items = sorted(freq.items(), key=lambda x: -x[1])

print("\nSorted by frequency:")
for item, count in sorted_items:
    print(item, count)
