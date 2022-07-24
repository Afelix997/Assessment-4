function newCat(){
    title = document.getElementById("newTitle").value

    axios.post("", {title : title}).then((response) => {
      window.location.href = "../../"
      })
  
  }
  