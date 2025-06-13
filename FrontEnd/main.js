document.getElementById("contact-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const status = document.getElementById("status");
  const form = e.target;
  const formData = new FormData(form);

  // Réinitialiser l'état
  status.innerText = "";
  status.classList.remove("success", "error");
  console.log("Formulaire soumis, début du traitement...");

  try {
    // Étape 1 : Récupérer le jeton CSRF
    console.log("Tentative de récupération du jeton CSRF...");
    let tokenResponse;
    try {
      tokenResponse = await fetch("http://localhost:5000/csrf-token", {
        method: "GET",
        headers: {
          "Accept": "application/json"
        }
      });
      console.log("Réponse CSRF reçue, statut :", tokenResponse.status);
      if (!tokenResponse.ok) {
        throw new Error(`Erreur HTTP ${tokenResponse.status}: Impossible d'obtenir le jeton CSRF`);
      }
    } catch (tokenError) {
      console.error("Erreur CSRF:", tokenError);
      status.innerText = "Erreur : Impossible de récupérer le jeton CSRF. Vérifiez si le serveur est en cours d'exécution sur http://localhost:5000.";
      status.classList.add("error");
      return;
    }

    const tokenData = await tokenResponse.json();
    console.log("Jeton CSRF reçu :", tokenData.csrf_token);
    if (!tokenData.csrf_token) {
      throw new Error("Jeton CSRF non reçu du serveur");
    }

    // Étape 2 : Préparer les données du formulaire
    const data = {
      name: formData.get("name"),
      email: formData.get("email"),
      message: formData.get("message"),
      csrf_token: tokenData.csrf_token
    };
    console.log("Données à envoyer :", data);

    // Étape 3 : Envoyer la requête POST
    console.log("Envoi de la requête POST à /contact/...");
    const response = await fetch("http://localhost:5000/contact/", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      }
    });

    console.log("Réponse POST reçue, statut :", response.status);
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.message || `Erreur HTTP ${response.status}`);
    }

    const result = await response.json();
    console.log("Résultat de la requête :", result);
    status.innerText = result.message || "Message envoyé avec succès !";
    status.classList.add("success");
    form.reset();
  } catch (error) {
    console.error("Erreur réseau:", error);
    let errorMessage = "Erreur : Impossible d’envoyer le message. ";
    if (error.message.includes("Failed to fetch")) {
      errorMessage += "Vérifiez si l'endpoint /contact/ est accessible et si le serveur Flask est en cours d'exécution.";
    } else if (error.message.includes("CORS")) {
      errorMessage += "Problème de CORS. Vérifiez la configuration CORS dans le backend.";
    } else {
      errorMessage += error.message;
    }
    status.innerText = errorMessage;
    status.classList.add("error");
  }
});