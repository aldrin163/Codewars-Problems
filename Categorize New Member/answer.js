function openOrSenior(data) {
  return data.map(([age, handicap]) => { // using array destructuring
    if (age >= 55 && handicap > 7) return "Senior";
    return "Open";
  });
}
