function revealMessage() {
    var message = document.getElementById("hiddenMessage");
    message.style.display = "block";
  }
  
  var button = document.getElementById("revealButton");
  button.onclick = revealMessage;
  