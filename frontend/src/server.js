const express = require("express");
import axios from "./axios";
const cors = require("cors");

const app = express();
const port = 5173;

app.use(cors());

app.get("/api/place-details", async (req, res) => {
	const { place_id } = req.query;
	try {
		const response = await axios.get(
			"https://maps.googleapis.com/maps/api/place/details/json",
			{
				params: {
					place_id,
					key: "AIzaSyAGNh44Urq3R3CJWtWYcAsvtRiwwupo-5s",
				},
			}
		);
		res.json(response.data);
	} catch (error) {
		res.status(500).json({ error: error.message });
	}
});

app.listen(port, () => {
	console.log(`Server running at http://localhost:${port}`);
});
