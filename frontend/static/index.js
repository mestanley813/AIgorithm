window.onload =  function() {
    let greeting = document.getElementById("greeting");
    const d = new Date();
    let hour = d.getHours();

    if (hour >= 5 && hour < 12) {
        greeting.innerHTML = "Good morning!";
    }

    else if (hour >= 12 && hour < 17) {
        greeting.innerHTML = "Good afternoon!";
    }

    else {
        greeting.innerHTML = "Good evening!";
    }
    
    let money = document.getElementById("balance");
    if (!document.getElementById("gain")) {
        money.style.color = "red";
    }
    else {
        money.style.color = "green";
    }
    }