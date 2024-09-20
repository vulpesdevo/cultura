const express = require("express");
const { createProxyMiddleware } = require("http-proxy-middleware");

const app = express();

// Proxy configuration
app.use(
	"/api",
	createProxyMiddleware({
		target: "https://serpapi.com",
		changeOrigin: true,
		pathRewrite: {
			"^/api": "", // remove /api prefix when forwarding to target
		},
		onProxyReq: (proxyReq, req, res) => {
			// Add any custom headers if needed
			proxyReq.setHeader(
				"x-api-key",
				"5394dbdebc3e75f87956b173bc7ef5c974793bbd67b24d19f12e68125a8d94f7"
			);
		},
	})
);

const PORT = process.env.PORT || 5173;
app.listen(PORT, () => {
	console.log(`Proxy server is running on http://localhost:${PORT}`);
});
