name = input("Enter file:")
if len(name) < 1:
    name = "esqimo_input.txt"
handle = open(name)
list_of_urls = []

for line in handle:
    line = line.strip()
    if not line.startswith('- http'):
        continue
    print(line)
    list_0 = line.split()  # here we break the line in words
    print(list_0)
    list_of_urls.append(list_0[1])

print(list_of_urls)
