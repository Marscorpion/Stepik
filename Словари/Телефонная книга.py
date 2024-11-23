n = int(input())

contacts = {}

for _ in range(n):
    phone, name=input().lower().split()
    contacts.setdefault(name, []).append(phone)

m = int(input())

for _ in range(m):
    c = input().lower()
    print(*contacts.get(c, ['абонент не найден']))




