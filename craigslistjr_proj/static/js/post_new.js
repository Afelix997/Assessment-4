function newPost(){
    // Remember to add '.value'
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDesc").value
    posted_by = document.getElementById("newPostBy").value
    email= document.getElementById("newEmail").value
    // "" is re-running this url but now in a POST request
    axios.post("", {title : title,description: description,posted_by: posted_by,email:email}).then((response) => {
      // Redirecting from JS based on your current url
      // Example: if current url = "genres/books/2/"
      // ../../ will cut off two of the last snippets of your url and run "genres/"
      window.location.href = "../view"
      })
  
  }