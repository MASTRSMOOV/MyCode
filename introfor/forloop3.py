#!/usr/bin/env python3

# A list called farms

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for farm in farms:
    print(f"The {farm['name']} has: {farm['agriculture']}")
    print(f"The {farm['name']} has:")
    
