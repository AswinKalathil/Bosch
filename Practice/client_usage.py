import tem_conversion

cel = eval(input("Enter Temp in celcious: "))
fah = tem_conversion.ctof(cel)

print("Temp in Farenheat: "+str(fah))