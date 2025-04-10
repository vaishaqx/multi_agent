document.querySelector("form").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const userInput = document.getElementById("user-input").value;
  
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userInput }),
    });
  
    const data = await response.json();
  
    const chatBox = document.querySelector(".chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
  
    document.getElementById("user-input").value = "";
  });
  