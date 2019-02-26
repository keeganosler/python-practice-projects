def can_fit(s1, s2, r1, r2):
    rec_area = r1*r2
    squares_area = s1 + s2
    if(squares_area <= rec_area):
        print("The squares will fit!")
    else:
        print("The squares won't fit!")

can_fit(10, 12, 4, 5) #failed case
can_fit(10, 10, 4, 5) #edge case
can_fit(10, 5, 4, 5) #success case