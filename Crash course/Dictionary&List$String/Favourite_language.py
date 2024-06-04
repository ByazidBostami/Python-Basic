favourite_language={"jen":["python","rubi"],"sara":["c"],"Edward":["rubi","go"],"phill":["python","haskell"]}

for key,value in favourite_language.items():
    print(f"\n{key.title()}'s favourite languages are:")
    for i in value:
        print(f"\t{i.title()}")
        