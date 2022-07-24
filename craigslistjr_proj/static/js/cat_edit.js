function deleteCat() {
    id = document.getElementById("id").value

    axios.post("", {id : id}).then((response) => {
      window.location.href = "../../../"
      })
}
function editCat() {
    title = document.getElementById("newTitle").value

    axios.put("", {title : title}).then((response) => {
      window.location.href = "../../../"
      })
  
  }
  