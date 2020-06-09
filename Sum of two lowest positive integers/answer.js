function sumTwoSmallestNumbers(numbers) {
  let sorted = numbers.sort((a, b) => a - b); // sorting in ascending order
  return sorted[0] + sorted[1];
}
