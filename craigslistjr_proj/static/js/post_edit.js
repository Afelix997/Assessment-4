function deletePost() {
    id = document.getElementById("id").value

    axios.post("", {id : id}).then((response) => {
      window.location.href = "../../view"
      })
}
function editPost() {
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDesc").value
    posted_by = document.getElementById("newPostBy").value
    email= document.getElementById("newEmail").value
    axios.put("", {title : title,description: description,posted_by: posted_by,email:email}).then((response) => {
      window.location.href = "../../view"
      })
  
  }
  