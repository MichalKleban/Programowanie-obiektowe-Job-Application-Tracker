document.addEventListener("DOMContentLoaded", function () {
    // Pobierz elementy formularza i przycisku do przełączania
    var form = document.getElementById("applicationForm");
    var toggleButton = document.getElementById("toggleForm");

    // Dodaj obsługę zdarzenia kliknięcia na przycisku
    toggleButton.addEventListener("click", function () {
        // Toggle the "hidden" class to show/hide the form
        form.classList.toggle("hidden");
    });
});