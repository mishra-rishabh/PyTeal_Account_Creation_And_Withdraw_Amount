from pyteal import *
from decouple import config

senderAddr = config( "SENDER" )
receiverAddr = config( "RECEIVER" )

def withdraw_program( receiverAddr ):
  """ Only allow receiver to withdraw funds from this account """
  withdrawAlgo = And(
    Txn.type_enum() == TxnType.Payment ,
    # Txn.type_enum == Int( 1 ) ,
    Txn.receiver() == Addr( receiverAddr ) ,
    Txn.sender() == Addr( senderAddr ) ,
    Global.group_size() == Int( 1 ) ,
    Txn.amount() == Int( 2000 ) ,
    Txn.close_remainder_to() == Addr( senderAddr ) ,
    Txn.asset_close_to() == Addr( senderAddr )
  )

  return withdrawAlgo

def clearState():
  program = Return( 1 )
  return compileTeal( program , Mode.Application )

if __name__ == "__main__":
  with open( "tealFiles/withdraw.teal" , "w" ) as f:
    compiled = compileTeal( withdraw_program( receiverAddr ) , Mode.Application )
    f.write( compiled )