cet = set(input("Enter CET students (comma-separated): ").split(","))
jee = set(input("Enter JEE students: ").split(","))
neet = set(input("Enter NEET students: ").split(","))

print("Union:", cet | jee | neet)
print("Intersection:", cet & jee & neet)
print("CET - JEE:", cet - jee)
