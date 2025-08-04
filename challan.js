function submitChallan() {
    const vehicleNumber = document.getElementById('vehicleNumber').value;
    const violationType = document.getElementById('violationType').value;
    const fineAmount = document.getElementById('fineAmount').value;


    window.location.href = `response.html?vehicleNumber=${vehicleNumber}&violationType=${violationType}&fineAmount=${fineAmount}`;
}