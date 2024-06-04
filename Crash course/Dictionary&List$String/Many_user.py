user={
    "Byazid":{"first":"Byazid",
                "Last":"Bostami",
                "Location":"Jamalpur"},
        "Tasfia":{"first":"Tasnim Sarowyer",
                  "Last":"Tasfia",
                  "Location":"Bramonbaria"}
                  }
for key,value in user.items():
    print(f"Username: {key}")
    full_name=value["first"]+" "+value["Last"]
    locations=value["Location"]
    print(f"\tFull name: {full_name} \tLocation: {locations}")