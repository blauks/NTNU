function followUser(username) {
  let followButton = document.getElementById("followButton");
  if (followButton.innerText !== "Follow") return;
  alert(`You just followed ${username}`);
  followButton.innerText = "Message";
  followButton.style.color = "black";
  followButton.style.backgroundColor = "white";
  followButton.style.border = "0.5px gray solid";
  followButton.style.fontWeight = "600";
}

function openDetailedView(id) {
  let background = document.getElementById("background");
  let openPost = document.getElementsByClassName("x")[0];
  background.style.display = "block";
  openPost.style.display = "block";
}

function closeOpenPost(id) {
  let background = document.getElementById("background");
  let openPosts = document.getElementsByClassName("x");
  background.style.display = "none";
  for (var i = 0; i < openPosts.length; i++) {
    openPosts[i].style.display = "none";
  }
}
