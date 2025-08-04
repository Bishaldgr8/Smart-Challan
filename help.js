document.getElementById("suggestionForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting normally
    
    // Get form values
    var email = document.getElementById("email").value;
    var suggestion = document.getElementById("suggestion").value;

    // Display the values (You'd normally send these values to a server for processing)
    console.log("Email: " + email);
    console.log("Suggestion: " + suggestion);

    // Clear form fields after submission (optional)
    document.getElementById("email").value = "";
    document.getElementById("suggestion").value = "";

    // Display a confirmation message (you'd normally handle this differently)
    alert("Thank you for your suggestion!");
});
