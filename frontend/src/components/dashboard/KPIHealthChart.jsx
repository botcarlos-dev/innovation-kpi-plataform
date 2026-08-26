import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";


function KPIHealthChart({ measurements }) {
  const healthyCount =
    measurements.filter(
      (measurement) =>
        measurement.status === "HEALTHY"
    ).length;

  const warningCount =
    measurements.filter(
      (measurement) =>
        measurement.status === "WARNING"
    ).length;

  const criticalCount =
    measurements.filter(
      (measurement) =>
        measurement.status === "CRITICAL"
    ).length;


  const data = [
    {
      name: "Healthy",
      value: healthyCount,
    },
    {
      name: "Warning",
      value: warningCount,
    },
    {
      name: "Critical",
      value: criticalCount,
    },
  ];


  return (
    <div className="chart-container">
      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <BarChart data={data}>
          <CartesianGrid
            strokeDasharray="3 3"
          />

          <XAxis dataKey="name" />

          <YAxis
            allowDecimals={false}
          />

          <Tooltip />

          <Bar
            dataKey="value"
            radius={[6, 6, 0, 0]}
          />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default KPIHealthChart;
