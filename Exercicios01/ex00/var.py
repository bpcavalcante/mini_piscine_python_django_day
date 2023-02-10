def my_var():
    var1 = 42
    var2 = "42"
    var3 = "quarante-deux"
    var4 = 42.0
    var5 = True
    var6 = [42]
    var7 = {42: 42}
    var8 = (42,)
    var9 = set()

    print(var1 , "tem um tipo" , var1.__class__)
    print(var2 , "tem um tipo" , var2.__class__)
    print(var3 , "tem um tipo", var3.__class__)
    print(var4 , "tem um tipo" , var4.__class__)
    print(var5 , "tem um tipo" , var5.__class__)
    print(var6 , "tem um tipo" , var6.__class__)
    print(var7 , "tem um tipo" , var7.__class__)
    print(var8 , "tem um tipo" , var8.__class__)
    print(var9 , "tem um tipo" , var9.__class__)

if __name__ == '__main__':  
    my_var()