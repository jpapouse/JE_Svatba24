function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block"
    }
  }

  function saveData() {
    const Jméno = document.getElementById('Jméno').value;
    const Příjmení = document.getElementById('Příjmení').value;
    const Telefon = document.getElementById('Telefon').value;
    const Email = document.getElementById('Email').value;
    const Intolerance = document.getElementById('Intolerance').value;
    const Vegetarian = document.getElementById('Vegetarian').value;
    const Alkohol = document.getElementById('Alkohol').value;
    const Nocleh = document.getElementById('Nocleh').value;
    const Tipy = document.getElementById('Tipy').value;
    const Pisne = document.getElementById('Pisne').value;

    // Create the request body object
    const requestBody = {
        "body":{
        Jmeno: Jméno,
        Prijmeni: Příjmení,
        Email: Email,
        Telefon: Telefon,
        Intolerance: Intolerance,
        Vegetarian: Vegetarian,
        Alkohol: Alkohol,
        Nocovani: Nocleh,
        Tipy: Tipy,
        Pisne: Pisne}
    };
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "text/plain");
    // Send the POST request
    fetch('https://xx3m1bkvd4.execute-api.eu-central-1.amazonaws.com/ProdApi', {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(requestBody),
        redirect: 'follow'
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data saved successfully:', data);
        alert("Úspěšně uloženo!");
        window.location.reload();
    })
    .catch(error => {
        console.error('Error saving data:', error);
        alert("Problém s uložením - zkuste to znova, nebo kontaktujte správce systému")
        // Handle any errors that occurred during the POST request
        }
    )
}