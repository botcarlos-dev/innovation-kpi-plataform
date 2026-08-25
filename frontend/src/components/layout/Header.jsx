function Header() {
  return (
    <header className="header">
      <div>
        <h1>Innovation Management</h1>

        <p>
          Monitor projects, KPIs and innovation performance.
        </p>
      </div>

      <div className="header-actions">
        <button className="notification-button">
          Notifications
        </button>

        <div className="user-profile">
          <div className="user-avatar">
            AD
          </div>

          <div>
            <strong>Administrator</strong>
            <span>Platform Manager</span>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;
