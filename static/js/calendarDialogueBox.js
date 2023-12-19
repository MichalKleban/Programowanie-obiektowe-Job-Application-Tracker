function showDialogueWindow(date) {

    // Pobieramy div o klasie "mojaKlasa"
    let myDiv = document.querySelector(".calendarDialogue");


    // Zmień zawartość diva
    myDiv.innerHTML = "<p>"+date+"</p>";
}