document.getElementById("myForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;

    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
});
