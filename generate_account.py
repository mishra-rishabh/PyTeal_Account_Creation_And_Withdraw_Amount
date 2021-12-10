from algosdk import account , encoding

pvtKey , addr = account.generate_account()

print( "Private Key: " , pvtKey )
print( "Account Address: " , addr )

if encoding.is_valid_address( addr ):
  print( "The address is valid!" )
else:
  print( "Invalid Address!" )
