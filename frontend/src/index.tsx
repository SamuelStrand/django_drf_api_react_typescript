import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./index.css";
import "./css/bootstrap/bootstrap.css";
import "./css/font_zen/style.css";
import "./css/font_awesome/css/all.css";

const container = document.getElementById("root")!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
