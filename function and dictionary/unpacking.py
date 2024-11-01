book_info = (
("Best Mystery & Thriller","The Silent Patient",68821),
("Best Horror","The Institute",75717),
("Best History & Biography","The five",31783 ),
("Best Fiction","The Testaments",98291)
) 
for i in range(len(book_info)):
    name,book_name,vote = book_info[i]
    print(f"{book_name} won the '{name}' category with {vote} votes")