
weight = input("Weight: ")
pounds_or_kilo = input("(L)bs or (K)g: ")
if pounds_or_kilo == 'k' and 'K':
  kilo = float(weight) * 0.45
  print(kilo)
elif pounds_or_kilo == 'l' and 'L':
  pounds = float(weight) * 2.2
  print(pounds)