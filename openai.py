const axios = require("axios");

async function sendRequest() {
  // Set the API endpoint URL
  const endpointUrl = "https://api.openai.com/v1/models/<model_name>/versions/<model_version>/prompts/<prompt_id>";

  // Set the API key
  const apiKey = "<your_api_key>";

  // Set the request headers
  const headers = {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${apiKey}`
  };

  // Set the request body
  const data = {
    "model": "<model_name>",
    "prompt": "<prompt_text>",
    "temperature": 0.5
  };

  try {
    // Make the request
    const response = await axios.post(endpointUrl, data, {headers});

    // Print the response
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

sendRequest();
