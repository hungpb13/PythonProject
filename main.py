# Format specifiers = {value:flags}
# Format a value based on what flags are inserted

# :.(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center justify
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.123456
price2 = -43269245.34
price3 = 12.34

print(f"Price 1 = {price1:+.2f}")
print(f"Price 2 = {price2:+,}")
print(f"Price 3 = {price3:+010.0f}")