function StatusBadge({ status }) {
  const normalizedStatus = status?.toUpperCase();

  return (
    <span
      className={`status-badge status-${normalizedStatus?.toLowerCase()}`}
    >
      {normalizedStatus}
    </span>
  );
}

export default StatusBadge;
