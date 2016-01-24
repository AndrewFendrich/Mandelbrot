def mandel_pixel(c,n = 16):
    z = c   
    for i in range(n):
        a = z * z
        z=a + c
        if a.real  >= 4.:            
            return(i)
    return(0)