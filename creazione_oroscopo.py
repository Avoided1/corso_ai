import random

lavoro=random.randint(1,5)
studio=random.randint(1,5)
fortuna=random.randint(1,5)
amore=random.randint(1,5)
generale=(lavoro+studio+fortuna+amore)/4

print(f"lavoro {lavoro}")
print(f"studio {studio}")
print(f"fortuna {fortuna}")
print(f"amore {amore}")
print(f"generale {generale}")