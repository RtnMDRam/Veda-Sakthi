<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SME Panel Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f6f6f6;
    }
    .sme-panel {
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
      display: flex;
      flex-direction: column;
      margin: 40px auto;
      padding: 24px;
      max-width: 500px;
    }
    .sme-panel-header {
      font-size: 1.4em;
      font-weight: bold;
      margin-bottom: 16px;
      color: #252525;
    }
    .sme-panel-section {
      margin-bottom: 12px;
    }
    .sme-panel-section:last-child {
      margin-bottom: 0;
    }
    .sme-panel-label {
      font-weight: bold;
      color: #0072c6;
      margin-bottom: 4px;
    }
    .sme-panel-value {
      color: #252525;
    }
  </style>
</head>
<body>
  <div class="sme-panel">
    <div class="sme-panel-header">Subject Matter Expert Panel</div>
    <div class="sme-panel-section">
      <div class="sme-panel-label">Name:</div>
      <div class="sme-panel-value">TR Mr. Karthik</div>
    </div>
    <div class="sme-panel-section">
      <div class="sme-panel-label">Area of Expertise:</div>
      <div class="sme-panel-value">Education Content Development</div>
    </div>
    <div class="sme-panel-section">
      <div class="sme-panel-label">Contact:</div>
      <div class="sme-panel-value">karthik@example.com</div>
    </div>
  </div>
</body>
</html>
