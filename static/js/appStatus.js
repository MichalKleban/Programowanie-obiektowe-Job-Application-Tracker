const table = document.getElementById('myTable');
  const tds = table.getElementsByTagName('td');

  for (let i = 0; i < tds.length; i++) {
    const text = tds[i].innerText.trim().toLowerCase();

    switch (text) {
      case 'successful':
        tds[i].style.backgroundColor = 'rgb(66, 168, 65)';
        tds[i].style.color = 'white';
        break;
      case 'pending':
        tds[i].style.backgroundColor = 'rgb(247, 192, 0)';
        break;
      case 'declined':
        tds[i].style.backgroundColor = 'rgb(209, 47, 67)';
        tds[i].style.color = 'white';
        break;
      case 'meeting':
        tds[i].style.backgroundColor = 'rgb(60, 124, 255)';
        tds[i].style.color = 'white';
        break;
      default:
        // Do nothing for other cases
        break;
    }
  }