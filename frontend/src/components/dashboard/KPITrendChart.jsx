import { useMemo, useState } from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ReferenceLine,
} from "recharts";


function KPITrendChart({
  measurements,
  kpis,
}) {
  const [selectedKPI, setSelectedKPI] =
    useState("");


  const activeKPIs = useMemo(() => {
    return kpis.filter(
      (kpi) => kpi.is_active
    );
  }, [kpis]);


  const selectedKPIData = useMemo(() => {
    if (!selectedKPI) {
      return activeKPIs[0] || null;
    }

    return activeKPIs.find(
      (kpi) =>
        kpi.id === Number(selectedKPI)
    );
  }, [
    selectedKPI,
    activeKPIs,
  ]);


  const chartData = useMemo(() => {
    if (!selectedKPIData) {
      return [];
    }

    return measurements
      .filter(
        (measurement) =>
          measurement.kpi_id ===
          selectedKPIData.id
      )
      .sort(
        (a, b) =>
          new Date(a.measurement_date) -
          new Date(b.measurement_date)
      )
      .map((measurement) => ({
        date: new Date(
          measurement.measurement_date
        ).toLocaleDateString(
          "en-GB",
          {
            day: "2-digit",
            month: "short",
          }
        ),

        value: Number(
          measurement.value
        ),

        status: measurement.status,
      }));
  }, [
    measurements,
    selectedKPIData,
  ]);


  if (!selectedKPIData) {
    return (
      <div className="empty-state">
        No KPI data available.
      </div>
    );
  }


  return (
    <div className="kpi-trend-chart">

      <div className="chart-controls">

        <div className="chart-kpi-selector">

          <label htmlFor="kpi-select">
            Select KPI
          </label>

          <select
            id="kpi-select"
            value={
              selectedKPI ||
              selectedKPIData.id
            }
            onChange={(event) =>
              setSelectedKPI(
                event.target.value
              )
            }
          >
            {activeKPIs.map((kpi) => (
              <option
                key={kpi.id}
                value={kpi.id}
              >
                {kpi.name}
              </option>
            ))}
          </select>

        </div>


        <div className="chart-kpi-info">

          <span>
            Unit:
            {" "}
            <strong>
              {selectedKPIData.unit}
            </strong>
          </span>

          <span>
            Target:
            {" "}
            <strong>
              {selectedKPIData.target_value}
            </strong>
          </span>

        </div>

      </div>


      {chartData.length === 0 ? (
        <div className="empty-state">
          No historical measurements
          available for this KPI.
        </div>
      ) : (
        <div className="chart-container">

          <ResponsiveContainer
            width="100%"
            height={350}
          >

            <LineChart
              data={chartData}
            >

              <CartesianGrid
                strokeDasharray="3 3"
              />

              <XAxis
                dataKey="date"
              />

              <YAxis />

              <Tooltip />

              <ReferenceLine
                y={
                  Number(
                    selectedKPIData.target_value
                  )
                }
                label="Target"
              />

              <ReferenceLine
                y={
                  Number(
                    selectedKPIData.warning_threshold
                  )
                }
                label="Warning"
              />

              <ReferenceLine
                y={
                  Number(
                    selectedKPIData.critical_threshold
                  )
                }
                label="Critical"
              />

              <Line
                type="monotone"
                dataKey="value"
                strokeWidth={3}
                dot={{
                  r: 5,
                }}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>
      )}

    </div>
  );
}


export default KPITrendChart;
