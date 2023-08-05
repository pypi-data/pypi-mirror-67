function displayIfJsElements() {
  var elements = document.getElementsByClassName("display-if-js");
  [].forEach.call(elements, function(el) {
      el.style.display = 'block';
  });

  elements = document.getElementsByClassName("remove-if-js");
  [].forEach.call(elements, function(el) {
      el.style.display = 'none';
  });
}

displayIfJsElements();

document.querySelector("#decideur").addEventListener("click", () => {
    let div = document.querySelector(".decideurs .form");
    if(div.style.height === "0px"){
        div.style.height = "600px";
    }else{
        div.style.height = "0px";
    }
});