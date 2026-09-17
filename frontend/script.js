const input = document.getElementById("messageInput");
const sendButton = document.getElementById("sendButton");
const chatMessages = document.getElementById("chatMessages");
function addMessage(message, sender) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message", sender);
    messageDiv.textContent = message;

    chatMessages.appendChild(messageDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


async function sendMessage() {

    const message = input.value.trim();

   
    if (message === "") {
        return;
    }

    
    addMessage(message, "user");

  
    input.value = "";

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });


  
        if (!response.ok) {
            throw new Error("Server returned an error");
        }


       
        const data = await response.json();


       
        addMessage(data.answer, "bot");

    }

    catch (error) {

        console.error("Error connecting to FastAPI:", error);

        addMessage(
            "Sorry, I could not connect to the chatbot server.",
            "bot"
        );
    }
}


sendButton.addEventListener("click", sendMessage);



input.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});