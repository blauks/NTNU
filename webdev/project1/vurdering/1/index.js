const colors = ["#33FF6E", "#FFD133", "#FF336E", "#F633FF", "#33FFCE"];
let setColor = "lightBlue";
$(document).ready(function () {
  resizeSVG();
  $("#svg-artwork").click(function () {
    let color = colors[Math.floor(Math.random() * colors.length)];
    $("#svg-eye-right").attr("fill", color);
  });
  $("#canvas-artwork").click(function () {
    let color = colors[Math.floor(Math.random() * colors.length)];
    drawCanvas(color);
    setColor = color;
  });
  drawCanvas("lightblue");
});

$(window).resize(function () {
  //Call resizeSVG and drawCanvas every time the window size changes
  resizeSVG();
  drawCanvas(setColor);
});

function resizeSVG() {
  let headRadius = Math.min(
    $("#svg-artwork").height() / 2,
    $("#svg-artwork").width() / 2
  );
  //Change head size based on size of container
  $("#svg-head").attr("cx", $("#svg-artwork").width() / 2);
  $("#svg-head").attr("cy", $("#svg-artwork").height() / 2);
  $("#svg-head").attr("r", headRadius);

  //Scale and position eyes
  $(".svg-eye").attr("r", $("#svg-head").attr("r") / 5);
  $(".svg-eye").attr("cx", $("#svg-head").attr("cx"));
  $(".svg-eye").attr("cy", $("#svg-head").attr("cy"));

  //Position eyes individually
  $("#svg-eye-left").attr(
    "cx",
    Number($("#svg-head").attr("cx")) - Number(headRadius / 3)
  );
  $("#svg-eye-right").attr(
    "cx",
    Number($("#svg-head").attr("cx")) + Number(headRadius / 3)
  );

  //Position mouth
  $("#svg-mouth").attr("width", $("#svg-head").attr("r") / 1.5);
  $("#svg-mouth").attr("height", $("#svg-head").attr("r") / 4);
  $("#svg-mouth").attr(
    "x",
    $("#svg-head").attr("cx") - $("#svg-mouth").attr("width") / 2
  );
  $("#svg-mouth").attr(
    "y",
    Number($("#svg-head").attr("cy")) + Number(headRadius * 0.5)
  );
  $("#svg-mouth").attr("stroke-width", 5);
  $("#svg-mouth").attr("ry", 50);

  //Scale and position teeth
  $(".svg-teeth").attr("width", $("#svg-mouth").attr("width") / 5);
  $(".svg-teeth").attr("height", $("#svg-mouth").attr("height") / 2);
  $(".svg-teeth").attr(
    "x",
    Number($("#svg-mouth").attr("x")) +
      Number($("#svg-mouth").attr("width") / 2)
  );
  $(".svg-teeth").attr(
    "y",
    Number($("#svg-mouth").attr("y")) +
      Number($("#svg-mouth").attr("stroke-width") - 2)
  );

  //Make left teeth position correctly and taller than right teeth
  $("#svg-teeth-left").attr(
    "x",
    $("#svg-teeth-left").attr("x") - $("#svg-teeth-left").attr("width")
  );
  $("#svg-teeth-left").attr(
    "height",
    $("#svg-teeth-left").attr("height") * 1.4
  );
}

function drawCanvas(color) {
  const c = document.querySelector("#canvas-artwork");
  const ctx = c.getContext("2d");

  c.width = $("#canvas-artwork").width();
  c.height = $("#canvas-artwork").height();
  let headRadius = Math.min(
    $("#canvas-artwork").height() / 2,
    $("#canvas-artwork").width() / 2
  );
  ctx.strokeStyle = "#000";
  ctx.beginPath();

  //Draw head
  console.log($("#canvas-artwork").width());
  console.log(c.width);
  ctx.arc(
    Number($("#canvas-artwork").width() / 2),
    Number($("#canvas-artwork").height() / 2),
    headRadius,
    0,
    2 * Math.PI
  );
  ctx.fillStyle = "white";
  ctx.fill();

  //Draw eyes
  ctx.beginPath();

  ctx.arc(
    Number($("#canvas-artwork").width() / 2) - headRadius / 3,
    Number($("#canvas-artwork").height() / 2),
    headRadius / 5,
    0,
    2 * Math.PI
  );
  ctx.fillStyle = "black";
  ctx.fill();

  ctx.beginPath();

  ctx.arc(
    Number($("#canvas-artwork").width() / 2) + headRadius / 3,
    Number($("#canvas-artwork").height() / 2),
    headRadius / 5,
    0,
    2 * Math.PI
  );
  ctx.strokeStyle = "black";
  ctx.lineWidth = 2;
  ctx.stroke();
  ctx.fillStyle = color;
  ctx.fill();

  //draw mouth
  ctx.beginPath();
  ctx.lineJoin = "round";
  ctx.rect(
    Number($("#canvas-artwork").width() / 2) - headRadius / 3,
    Number($("#canvas-artwork").height() / 2 + headRadius / 2),
    headRadius / 1.5,
    headRadius / 4
  );
  ctx.fillStyle = "black";
  ctx.strokeStyle = "red";
  ctx.lineWidth = 5;
  ctx.fill();
  ctx.stroke();

  //Draw teeth
  ctx.beginPath();
  ctx.rect(
    Number($("#canvas-artwork").width() / 2) -
      headRadius / 3 +
      headRadius / 1.5 / 2,
    Number($("#canvas-artwork").height() / 2 + headRadius / 2) + 4,
    headRadius / 1.5 / 5,
    headRadius / 4 / 2
  );
  ctx.fillStyle = "white";
  ctx.strokeStyle = "black";
  ctx.lineWidth = "2";
  ctx.lineJoin = "miter";
  ctx.stroke();
  ctx.fill();

  ctx.beginPath();
  ctx.rect(
    Number($("#canvas-artwork").width() / 2) -
      headRadius / 3 +
      headRadius / 1.5 / 2 -
      headRadius / 1.5 / 5,
    Number($("#canvas-artwork").height() / 2 + headRadius / 2) + 4,
    headRadius / 1.5 / 5,
    (headRadius / 4 / 2) * 1.4
  );
  ctx.fillStyle = "white";
  ctx.strokeStyle = "black";
  ctx.lineWidth = "2";
  ctx.lineJoin = "miter";
  ctx.stroke();
  ctx.fill();
}
let documentationVisibility = false;
$("#show-docs-button").click(function () {
  if (!documentationVisibility) {
    $("#documentation").show();
    $("#show-docs-button").html("Hide documentation");
    documentationVisibility = true;
  } else {
    $("#documentation").hide();
    $("#show-docs-button").html("Show documentation");
    documentationVisibility = false;
  }
});
