function exercise7(amount,coins) {
    if (amount === 0 && coins === 0) {
      return true;
    } else if (amount < 0 || coins < 0) {
      return false;
    } else {
      return exercise7(amount - 200, coins - 1) || exercise7(amount - 100, coins - 1) 
      || exercise7(amount - 50, coins - 1) || exercise7(amount - 20, coins - 1) 
      || exercise7(amount - 10, coins - 1) || exercise7(amount - 5, coins - 1) 
      || exercise7(amount - 2, coins - 1) || exercise7(amount - 1, coins - 1);
    }
  }



