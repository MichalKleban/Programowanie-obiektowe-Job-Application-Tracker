let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

const day = document.querySelector(".calendar-dates");

const currdate = document.querySelector(".calendar-current-date");

const prenexIcons = document.querySelectorAll(".calendar-navigation span");

// Array of month names
const months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
];

// Function to generate the calendar
const manipulate = () => {

	// Get the first day of the month
	let dayone = new Date(year, month, 1).getDay();

	// Get the last date of the month
	let lastdate = new Date(year, month + 1, 0).getDate();

	// Get the day of the last date of the month
	let dayend = new Date(year, month, lastdate).getDay();

	// Get the last date of the previous month
	let monthlastdate = new Date(year, month, 0).getDate();

	// Variable to store the generated calendar HTML
	let lit = "";

	// Loop to add the last dates of the previous month
	for (let i = dayone; i > 0; i--) {
		lit +=
			`<li class="inactive">${monthlastdate - i + 1}</li>`;
	}

	
	var inputString = document.getElementById('daysToHighlight').innerHTML;

	// Usuń wszystkie znaki, które nie są cyframi, myślnikiem, ani przecinkiem
	var cleanedString = inputString.replace(/[^\d,-]/g, '');
	
	// Podziel ciąg znaków na tablicę, używając przecinka jako separatora
	var dataArray = cleanedString.split(',');
	
	// Filtruj tylko elementy, które są datami
	var dateArray = dataArray.filter(function(item) {
	  // Sprawdź, czy element pasuje do formatu daty YYYY-MM-DD
	  return /\d{4}-\d{2}-\d{2}/.test(item);
	});

	console.log(dateArray);

	for (var i = 0; i < dateArray.length; i+=1) {
		var elementId = dataArray[i];
		console.log(elementId)
		var element = document.getElementById(elementId);
	
		if (element) {
			
			element.style.backgroundColor = "black";
		} else {
			console.error("Element o ID " + dateArray[i] + " nie został znaleziony.");
		}
	}
	

	for (let i = 1; i <= lastdate; i++) {

		// Check if the current date is today
		let isToday = i === date.getDate()
			&& month === new Date().getMonth()
			&& year === new Date().getFullYear()
			? "active"
			: "";
		lit += `<li id="${year}-${month}-${i.toString().padStart(2, '0')}" class="${isToday}"><a onclick="showDialogueWindow('${year}-${month}-${i}')" >${i}</a></li>`;
	}

	// Loop to add the first dates of the next month
	for (let i = dayend; i < 6; i++) {
		lit += `<li class="inactive">${i - dayend + 1}</li>`
	}

	// Update the text of the current date element 
	// with the formatted current month and year
	currdate.innerText = `${months[month]} ${year}`;

	// update the HTML of the dates element 
	// with the generated calendar
	day.innerHTML = lit;
}

manipulate();

// Attach a click event listener to each icon
prenexIcons.forEach(icon => {

	// When an icon is clicked
	icon.addEventListener("click", () => {

		// Check if the icon is "calendar-prev"
		// or "calendar-next"
		month = icon.id === "calendar-prev" ? month - 1 : month + 1;

		// Check if the month is out of range
		if (month < 0 || month > 11) {

			// Set the date to the first day of the 
			// month with the new year
			date = new Date(year, month, new Date().getDate());

			// Set the year to the new year
			year = date.getFullYear();

			// Set the month to the new month
			month = date.getMonth();
		}

		else {

			// Set the date to the current date
			date = new Date();
		}

		// Call the manipulate function to 
		// update the calendar display
		manipulate();
	});
});

console.log("działa fpskfsefs")