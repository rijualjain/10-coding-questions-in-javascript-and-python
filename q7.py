def exercise7(amount, coins):
  
  amount_pence = amount * 100
  
  coins_pence = [200, 100, 50, 20, 10, 5, 2, 1]

  def helper(amount_pence, coins, num_coins):

    if amount_pence == 0:
      return True

    if num_coins == 0:
      return False
  
    for coin_pence in coins_pence:
  
      if coin_pence > amount_pence:
        continue
      if helper(amount_pence - coin_pence, coins, num_coins - 1):
        return True
    return False
  
  return helper(amount_pence, coins, coins)
print(exercise7(3, 2))  
print(exercise7(5, 3))  



