function newPost(){
   
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDesc").value
    posted_by = document.getElementById("newPostBy").value
    email= document.getElementById("newEmail").value
    
    axios.post("", {title : title,description: description,posted_by: posted_by,email:email}).then((response) => {
    
      window.location.href = "../view"
      })
  
  }