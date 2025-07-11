const express = require("express");
const { OpenAI } = require("openai");
const cors = require("cors");

const app = express();
const port = 3000;

// Middleware
app.use(express.json());
app.use(cors());

// Initialiser OpenAI
const openai = new OpenAI({
  apiKey: "sk-proj-e6xTlVJVn7mqApjJJM76T3BlbkFJRtsDFAFuM5I1YPhLKctV",
  dangerouslyAllowBrowser: true,
});

// Endpoint pour communiquer avec OpenAI
app.post("/api/analyze", async (req, res) => {
  const { message } = req.body;

  try {
    const response = await openai.chat.completions.create({
      messages: [{ role: "user", content: message }],
      model: "gpt-3.5-turbo-0125",
      max_tokens: 512,
      temperature: 0.7,
    });

    const result = response.choices[0]?.message?.content || "No response.";
    res.json({ success: true, result });
  } catch (error) {
    console.error("Error communicating with OpenAI:", error);
    res
      .status(500)
      .json({ success: false, error: "Failed to process request" });
  }
});

// Démarrer le serveur
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
