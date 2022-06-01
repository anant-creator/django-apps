const randInt = function (min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
};

const randColor = function () {
  return `rgb(${randInt(0, 255)}, ${randInt(0, 255)}, ${randInt(0, 255)})`;
};

const quer = document.querySelector("h2");
console.log(randColor());
quer.style.color = `${randColor()}`;
