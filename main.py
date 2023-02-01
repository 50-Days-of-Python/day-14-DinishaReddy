def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for i in l:
        for k in i:
         sdl.append(k)
    # Insert Code Above
    # Return single-dimension list.
    return sdl
