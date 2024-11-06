function toggleDiv() {
    const extraContent = document.querySelector(".extra-content");
    const button = document.querySelector(".toggle-button");
    if (extraContent.style.display === "none" || extraContent.style.display === "") {
        extraContent.style.display = "block";
        button.innerHTML = "&#9650;"; // Muda para seta para cima
    } else {
        extraContent.style.display = "none";
        button.innerHTML = "&#9660;"; // Muda para seta para baixo
    }
}
