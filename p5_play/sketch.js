function setup() {
  colorMode(HSB, 360, 100, 100, 100);
  createCanvas(640, 480);
  background('#efefef');
}

function draw() {
  fill(255);
  ellipse(mouseX, mouseY, 80, 80);
}

function mouseClicked(){
  save('screenshot.png');
  return false;
}
