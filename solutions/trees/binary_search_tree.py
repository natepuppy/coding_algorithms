

# --- Test ---
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)

print(search(root, 20))   # True
print(search(root, 99))   # False
root = delete(root, 30)
print(search(root, 30))   # False
