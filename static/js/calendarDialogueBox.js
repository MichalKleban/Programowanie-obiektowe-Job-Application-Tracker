function showDialogueWindow(date) {

    // Pobieramy div o klasie "mojaKlasa"
    let myDiv = document.querySelector(".calendarDialogue");
    const table = document.getElementById('myTable');
    const trs = table.getElementsByTagName('tr');
    const tds = table.getElementsByTagName('td');
    var found = [] 

    for (let i = 0; i < trs.length; i++) {
        const text = trs[i].innerText.trim().toLowerCase();
        if(text.includes(date)){
            console.log(text)
            found.push(trs[i])
        }else {
            console.log("Nie ma daty")
        }
    }
    
    document.getElementById("info").innerText = "";

    for (let i = 0; i < found.length; i++) {
        var orginalnyELE = found[i]
        var skopiowanyELE = orginalnyELE.cloneNode(true)
        document.getElementById("info").appendChild(skopiowanyELE)
    }
    
    
    

}