import api from "./client";

export async function getMeasurements() {
  const response = await api.get(
    "/kpi-measurements/"
  );

  return response.data;
}
