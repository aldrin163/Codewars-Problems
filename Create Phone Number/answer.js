function createPhoneNumber(numbers) {
  let ans = "(";
  for (let i = 0; i < 10; i++) {
    ans += numbers[i];
    if (i == 2) ans += ") ";
    else if (i == 5) ans += "-";
  }
  return ans;
}
