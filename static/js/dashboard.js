const form = document.getElementById("resumeForm");

form.addEventListener("submit", async function(e) {

    e.preventDefault();

    const formData = new FormData();

    const fileInput = document.getElementById("resume");

    formData.append(
        "resume",
        fileInput.files[0]
    );

    const response = await fetch(
        "/upload_resume",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    document.getElementById("resume_score").innerText = data.resume_score;

    document.getElementById("role").innerText = data.role;

    document.getElementById("match_score").innerText = data.match_score;

    document.getElementById("salary").innerText = data.salary;

    document.getElementById("retention").innerText = data.retention;

    document.getElementById("ranking").innerText = data.ranking;

});