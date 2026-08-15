"""
FastAPI API Server

Provides HTTP endpoints for controlling and monitoring
the pool motor.
"""

from fastapi import FastAPI

from src.controller.motor_controller import MotorController
from src.hardware.motor import Motor
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pool Controller")


# Hardware
motor = Motor()

# Business Logic
motor_controller = MotorController(motor)


@app.get("/")
def home():
    return {
        "project": "Pool Controller",
        "status": "Running"
    }


@app.post("/motor/on")
def motor_on():
    motor_controller.start()

    return {
        "motor": "ON"
    }


@app.post("/motor/off")
def motor_off():
    motor_controller.stop()

    return {
        "motor": "OFF"
    }


@app.get("/motor/status")
def motor_status():
    return motor_controller.status()


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>Pool Controller</title>

        <style>

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }


            body {
                min-height: 100vh;

                font-family:
                    Arial,
                    Helvetica,
                    sans-serif;

                background: #eef2f7;

                display: flex;
                justify-content: center;
                align-items: center;

                padding: 20px;

                color: #1f2937;
            }


            .dashboard {
                width: 100%;
                max-width: 900px;
            }


            .header {
                margin-bottom: 20px;
            }


            .header h1 {
                font-size: 28px;
                margin-bottom: 6px;
            }


            .header p {
                color: #6b7280;
                font-size: 14px;
            }


            .card {
                background: white;

                border-radius: 18px;

                padding: 24px;

                box-shadow:
                    0 8px 30px
                    rgba(15, 23, 42, 0.08);
            }


            .status-card {
                text-align: center;

                margin-bottom: 20px;
            }


            .status-label {
                color: #6b7280;

                font-size: 14px;

                margin-bottom: 12px;
            }


            #status {
                font-size: 32px;

                font-weight: 700;

                margin-bottom: 10px;
            }


            #last-update {
                color: #9ca3af;

                font-size: 13px;
            }


            .status-running {
                color: #16a34a;
            }


            .status-stopped {
                color: #dc2626;
            }


            .controls {
                display: grid;

                grid-template-columns:
                    repeat(2, 1fr);

                gap: 14px;
            }


            button {
                border: none;

                border-radius: 12px;

                padding: 16px;

                font-size: 16px;

                font-weight: 700;

                cursor: pointer;

                transition:
                    transform 0.15s ease,
                    opacity 0.15s ease;
            }


            button:hover {
                transform: translateY(-1px);
            }


            button:active {
                transform: translateY(1px);
            }


            button:disabled {
                opacity: 0.5;

                cursor: not-allowed;

                transform: none;
            }


            .on {
                background: #16a34a;

                color: white;
            }


            .off {
                background: #dc2626;

                color: white;
            }


            .info-grid {
                display: grid;

                grid-template-columns:
                    repeat(2, 1fr);

                gap: 14px;

                margin-top: 20px;
            }


            .info-card {
                background: #f8fafc;

                border-radius: 12px;

                padding: 18px;
            }


            .info-title {
                font-size: 13px;

                color: #6b7280;

                margin-bottom: 6px;
            }


            .info-value {
                font-size: 18px;

                font-weight: 700;
            }


            .footer {
                text-align: center;

                margin-top: 18px;

                color: #9ca3af;

                font-size: 12px;
            }


            @media (max-width: 600px) {

                body {
                    align-items: flex-start;

                    padding: 16px;
                }


                .header h1 {
                    font-size: 24px;
                }


                .card {
                    padding: 20px;

                    border-radius: 15px;
                }


                #status {
                    font-size: 28px;
                }


                .controls {
                    grid-template-columns: 1fr;
                }


                button {
                    width: 100%;

                    padding: 17px;
                }


                .info-grid {
                    grid-template-columns: 1fr;
                }

            }

        </style>

    </head>


    <body>

        <main class="dashboard">

            <header class="header">

                <h1>Pool Controller</h1>

                <p>
                    Residential pool motor control system
                </p>

            </header>


            <section class="card status-card">

                <div class="status-label">
                    MOTOR STATUS
                </div>


                <div id="status">
                    Loading...
                </div>


                <div id="last-update">
                    Waiting for status...
                </div>

            </section>


            <section class="card">

                <div class="controls">

                    <button
                        id="on-button"
                        class="on"
                        onclick="turnMotorOn()"
                    >
                        TURN ON
                    </button>


                    <button
                        id="off-button"
                        class="off"
                        onclick="turnMotorOff()"
                    >
                        TURN OFF
                    </button>

                </div>


                <div class="info-grid">

                    <div class="info-card">

                        <div class="info-title">
                            CONTROL
                        </div>

                        <div class="info-value">
                            Manual
                        </div>

                    </div>


                    <div class="info-card">

                        <div class="info-title">
                            CONNECTION
                        </div>

                        <div
                            id="connection"
                            class="info-value"
                        >
                            Checking...
                        </div>

                    </div>

                </div>

            </section>


            <div class="footer">
                Pool Controller · MVP
            </div>

        </main>


        <script>

            async function updateStatus() {

                try {

                    const response =
                        await fetch("/motor/status");


                    if (!response.ok) {

                        throw new Error(
                            "Status request failed"
                        );

                    }


                    const data =
                        await response.json();


                    const status =
                        document.getElementById(
                            "status"
                        );


                    const lastUpdate =
                        document.getElementById(
                            "last-update"
                        );


                    const connection =
                        document.getElementById(
                            "connection"
                        );


                    const onButton =
                        document.getElementById(
                            "on-button"
                        );


                    const offButton =
                        document.getElementById(
                            "off-button"
                        );


                    connection.textContent =
                        "Connected";


                    connection.style.color =
                        "#16a34a";


                    if (data.running) {

                        status.textContent =
                            "🟢 RUNNING";

                        status.className =
                            "status-running";

                        onButton.disabled =
                            true;

                        offButton.disabled =
                            false;

                    } else {

                        status.textContent =
                            "🔴 STOPPED";

                        status.className =
                            "status-stopped";

                        onButton.disabled =
                            false;

                        offButton.disabled =
                            true;

                    }


                    lastUpdate.textContent =
                        "Last update: " +
                        new Date().toLocaleTimeString();

                }

                catch (error) {

                    console.error(
                        "Dashboard update failed:",
                        error
                    );


                    document.getElementById(
                        "connection"
                    ).textContent =
                        "Disconnected";


                    document.getElementById(
                        "connection"
                    ).style.color =
                        "#dc2626";

                }

            }


            async function turnMotorOn() {

                try {

                    await fetch(
                        "/motor/on",
                        {
                            method: "POST"
                        }
                    );


                    await updateStatus();

                }

                catch (error) {

                    console.error(
                        "Motor ON failed:",
                        error
                    );

                }

            }


            async function turnMotorOff() {

                try {

                    await fetch(
                        "/motor/off",
                        {
                            method: "POST"
                        }
                    );


                    await updateStatus();

                }

                catch (error) {

                    console.error(
                        "Motor OFF failed:",
                        error
                    );

                }

            }


            updateStatus();


            setInterval(
                updateStatus,
                5000
            );

        </script>

    </body>

    </html>
    """