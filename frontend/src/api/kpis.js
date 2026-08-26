import api from "./client";

export async function getKPIs() {
  const response = await api.get("/kpis/");

  return response.data;
}
