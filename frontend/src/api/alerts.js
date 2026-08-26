import api from "./client";

export async function getAlerts() {
  const response = await api.get("/alerts/");

  return response.data;
}

export async function getCriticalAlerts() {
  const response = await api.get(
    "/alerts/critical"
  );

  return response.data;
}
